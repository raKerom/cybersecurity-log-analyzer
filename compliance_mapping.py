
# Simple illustrative mapping to ISO 27001:2022 controls.
# Validate the mappings against the official standard before submission.

COMPLIANCE_MAP = {
    "login_failure": {
        "control": "ISO 27001:2022 Annex A 8.5",
        "control_name": "Secure authentication",
        "risk": "Repeated failed logins may indicate an attempted account compromise.",
        "remediation": "Review authentication logs, enforce MFA, and apply appropriate login rate limits."
    },
    "unauthorized_access": {
        "control": "ISO 27001:2022 Annex A 8.3",
        "control_name": "Information access restriction",
        "risk": "Unauthorized access may expose sensitive information.",
        "remediation": "Review access permissions and investigate the affected account and asset."
    },
    "privilege_escalation": {
        "control": "ISO 27001:2022 Annex A 8.2",
        "control_name": "Privileged access rights",
        "risk": "An attacker may gain elevated privileges.",
        "remediation": "Review privileged accounts, revoke unauthorized permissions, and investigate the activity."
    },
    "malware_alert": {
        "control": "ISO 27001:2022 Annex A 8.7",
        "control_name": "Protection against malware",
        "risk": "Malware may compromise systems or data.",
        "remediation": "Investigate the alert, isolate the affected system if warranted, and run approved security scans."
    },
    "port_scan": {
        "control": "ISO 27001:2022 Annex A 8.20",
        "control_name": "Network security",
        "risk": "Port scanning may indicate reconnaissance for vulnerable services.",
        "remediation": "Review network logs and restrict unnecessary exposed services."
    },
    "file_access": {
        "control": "ISO 27001:2022 Annex A 8.3",
        "control_name": "Information access restriction",
        "risk": "Unexpected file access may expose or modify sensitive information.",
        "remediation": "Verify whether the access was authorized and review relevant file permissions."
    }
}


def map_event(event_type):
    return COMPLIANCE_MAP.get(
        event_type,
        {
            "control": "Manual review required",
            "control_name": "Unmapped event",
            "risk": "The event has no configured compliance mapping.",
            "remediation": "Review the event and determine an appropriate control."
        }
    )


if __name__ == "__main__":
    for event in COMPLIANCE_MAP:
        print(event, "->", map_event(event)["control"])
