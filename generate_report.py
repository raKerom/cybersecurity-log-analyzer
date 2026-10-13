
import pandas as pd
from compliance_mapping import map_event

# Load correlated incidents
df = pd.read_csv("correlated_incidents.csv")

report_rows = []

for _, incident in df.iterrows():
    event_types = [
        event.strip()
        for event in str(incident["event_types"]).split(",")
    ]

    mappings = [map_event(event) for event in event_types]

    controls = sorted(set(
        mapping["control"] for mapping in mappings
    ))

    risks = sorted(set(
        mapping["risk"] for mapping in mappings
    ))

    remediations = sorted(set(
        mapping["remediation"] for mapping in mappings
    ))

    report_rows.append({
        "incident_id": incident["incident_id"],
        "source_ip": incident["source_ip"],
        "affected_asset": incident["affected_asset"],
        "first_seen": incident["first_seen"],
        "last_seen": incident["last_seen"],
        "event_count": incident["event_count"],
        "event_types": incident["event_types"],
        "severity": incident["max_severity"],
        "evidence": (
            f"Source IP: {incident['source_ip']}; "
            f"Asset: {incident['affected_asset']}; "
            f"Events: {incident['event_types']}; "
            f"Time range: {incident['first_seen']} "
            f"to {incident['last_seen']}"
        ),
        "compliance_controls": "; ".join(controls),
        "risk": " | ".join(risks),
        "remediation": " | ".join(remediations),
    })

report = pd.DataFrame(report_rows)

# Save structured report
report.to_csv("security_report.csv", index=False)

# Save a readable Markdown report
with open("security_report.md", "w", encoding="utf-8") as file:
    file.write("# Cybersecurity Log Analysis Report\n\n")
    file.write(
        "> Demonstration report generated from synthetic data. "
        "Incidents and asset assignments require validation.\n\n"
    )
    file.write(f"Potential incidents identified: {len(report)}\n\n")

    for _, row in report.iterrows():
        file.write(f"## Incident {row['incident_id']}\n\n")
        file.write(f"- **Severity:** {row['severity']}\n")
        file.write(f"- **Source IP:** {row['source_ip']}\n")
        file.write(f"- **Affected asset:** {row['affected_asset']}\n")
        file.write(f"- **First seen:** {row['first_seen']}\n")
        file.write(f"- **Last seen:** {row['last_seen']}\n")
        file.write(f"- **Event types:** {row['event_types']}\n")
        file.write(f"- **Evidence:** {row['evidence']}\n")
        file.write(
            f"- **Compliance controls:** "
            f"{row['compliance_controls']}\n"
        )
        file.write(f"- **Risk:** {row['risk']}\n")
        file.write(
            f"- **Recommended remediation:** "
            f"{row['remediation']}\n\n"
        )

print("Security report generated successfully.")
print("Incidents included:", len(report))
print("Files saved: security_report.csv, security_report.md")
