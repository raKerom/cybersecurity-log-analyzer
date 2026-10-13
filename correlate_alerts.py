
import pandas as pd

# Load processed security logs
df = pd.read_csv("processed_logs.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Keep suspicious events only
suspicious = df[df["label"] == "Suspicious"].copy()

# Sort events by source and time
suspicious = suspicious.sort_values(
    by=["source_ip", "timestamp"]
)

# Group related events by source IP and affected asset
suspicious["incident_id"] = (
    suspicious.groupby(["source_ip", "affected_asset"])
    .ngroup() + 1
)

# Summarize each potential incident
incidents = suspicious.groupby("incident_id").agg(
    source_ip=("source_ip", "first"),
    affected_asset=("affected_asset", "first"),
    first_seen=("timestamp", "min"),
    last_seen=("timestamp", "max"),
    event_count=("event_type", "count"),
    event_types=("event_type", lambda x: ", ".join(sorted(set(x)))),
    max_severity=("severity", "max"),
).reset_index()

print("Potential incidents found:", len(incidents))
print("\nIncident summary:")
print(incidents.to_string(index=False))

# Save results
incidents.to_csv("correlated_incidents.csv", index=False)
print("\nSaved as correlated_incidents.csv")
