
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from datetime import datetime

import pandas as pd
import joblib


# --------------------------------------------------
# 1. Initialize API and load the trained ML model
# --------------------------------------------------

app = FastAPI(
    title="Cybersecurity Log Analyzer API",
    description=(
        "API for detecting suspicious security logs "
        "and correlating potential incidents."
    ),
    version="1.0.0"
)

try:
    model = joblib.load("security_model.pkl")
    training_columns = model.feature_names_in_.tolist()
except (FileNotFoundError, AttributeError, ValueError) as exc:
    raise RuntimeError(
        "Could not load security_model.pkl. "
        "Run train_model.py first."
    ) from exc


# --------------------------------------------------
# 2. Define and validate incoming log data
# --------------------------------------------------

class SecurityLog(BaseModel):
    timestamp: datetime

    source_ip: str = Field(
        min_length=1,
        max_length=100
    )

    event_type: str = Field(
        min_length=1,
        max_length=100
    )

    failed_attempts: int = Field(
        ge=0,
        le=100000
    )

    severity: Literal[
        "low", "medium", "high", "critical"
    ]

    affected_asset: str = Field(
        min_length=1,
        max_length=100
    )


# --------------------------------------------------
# 3. Severity ranking helper
# --------------------------------------------------

SEVERITY_RANK = {
    "low": 1,
    "medium": 2,
    "high": 3,
    "critical": 4
}


def get_highest_severity(severities):
    """Return the highest severity in a group."""
    return max(
        severities,
        key=lambda severity: SEVERITY_RANK[severity]
    )


# --------------------------------------------------
# 4. Home endpoint
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Cybersecurity Log Analyzer API is running",
        "docs": "/docs"
    }


# --------------------------------------------------
# 5. Analyze logs and correlate suspicious events
# --------------------------------------------------

@app.post("/analyze")
def analyze_logs(logs: list[SecurityLog]):

    # Validate that at least one log was submitted
    if not logs:
        raise HTTPException(
            status_code=400,
            detail="Submit at least one log entry."
        )

    try:
        # Convert input logs into a DataFrame
        df = pd.DataFrame([
            log.model_dump()
            for log in logs
        ])

        # Ensure timestamps are valid
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="raise"
        )

        # Prepare the same features used during training
        features = df[
            [
                "event_type",
                "failed_attempts",
                "severity"
            ]
        ].copy()

        # Convert categorical features into numeric columns
        features = pd.get_dummies(
            features,
            columns=["event_type", "severity"],
            dtype=int
        )

        # Match the exact feature columns used by the model
        features = features.reindex(
            columns=training_columns,
            fill_value=0
        )

        # Make ML predictions
        predictions = model.predict(features)

        df["prediction"] = predictions

        # ------------------------------------------
        # 6. Select suspicious logs
        # ------------------------------------------

        suspicious = df[
            df["prediction"] == "Suspicious"
        ].copy()

        incidents = []

        # ------------------------------------------
        # 7. Correlate suspicious logs
        # ------------------------------------------

        if not suspicious.empty:

            # Group events by source IP and affected asset
            suspicious["incident_id"] = (
                suspicious.groupby(
                    ["source_ip", "affected_asset"],
                    sort=True
                ).ngroup() + 1
            )

            # Build an incident summary for each group
            for incident_id, group in suspicious.groupby(
                "incident_id",
                sort=True
            ):

                group = group.sort_values("timestamp")

                incidents.append({
                    "incident_id": int(incident_id),

                    "source_ip": str(
                        group["source_ip"].iloc[0]
                    ),

                    "affected_asset": str(
                        group["affected_asset"].iloc[0]
                    ),

                    "event_count": int(len(group)),

                    "event_types": sorted(
                        group["event_type"].unique().tolist()
                    ),

                    "first_seen": (
                        group["timestamp"].min().isoformat()
                    ),

                    "last_seen": (
                        group["timestamp"].max().isoformat()
                    ),

                    "max_severity": get_highest_severity(
                        group["severity"].tolist()
                    )
                })

        # ------------------------------------------
        # 8. Format individual log results
        # ------------------------------------------

        results = []

        for _, row in df.iterrows():
            results.append({
                "timestamp": row["timestamp"].isoformat(),
                "source_ip": row["source_ip"],
                "affected_asset": row["affected_asset"],
                "event_type": row["event_type"],
                "severity": row["severity"],
                "prediction": str(row["prediction"])
            })

        # ------------------------------------------
        # 9. Return detection and correlation results
        # ------------------------------------------

        return {
            "logs_analyzed": len(results),
            "suspicious_logs": len(suspicious),
            "potential_incident_count": len(incidents),
            "results": results,
            "potential_incidents": incidents
        }

    except (ValueError, TypeError, KeyError) as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Could not process log data: {exc}"
        ) from exc

    except Exception as exc:
        # Return a generic message without exposing internals
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred during log analysis."
        ) from exc
