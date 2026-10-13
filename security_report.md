# Cybersecurity Log Analysis Report

> Demonstration report generated from synthetic data. Incidents and asset assignments require validation.

Potential incidents identified: 56

## Incident 1

- **Severity:** high
- **Source IP:** 203.0.113.1
- **Affected asset:** database-01
- **First seen:** 2026-10-13 11:47:00
- **Last seen:** 2026-10-13 12:16:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.1; Asset: database-01; Events: login_failure, malware_alert; Time range: 2026-10-13 11:47:00 to 2026-10-13 12:16:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 2

- **Severity:** medium
- **Source IP:** 203.0.113.1
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 14:49:00
- **Last seen:** 2026-10-13 15:12:00
- **Event types:** file_access, login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.1; Asset: web-server-01; Events: file_access, login_failure, unauthorized_access; Time range: 2026-10-13 14:49:00 to 2026-10-13 15:12:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 3

- **Severity:** medium
- **Source IP:** 203.0.113.1
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:00:00
- **Last seen:** 2026-10-13 11:35:00
- **Event types:** login_success, malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.1; Asset: workstation-01; Events: login_success, malware_alert, unauthorized_access; Time range: 2026-10-13 09:00:00 to 2026-10-13 11:35:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7; Manual review required
- **Risk:** Malware may compromise systems or data. | The event has no configured compliance mapping. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset. | Review the event and determine an appropriate control.

## Incident 4

- **Severity:** high
- **Source IP:** 203.0.113.10
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 09:54:00
- **Last seen:** 2026-10-13 15:26:00
- **Event types:** login_failure, port_scan
- **Evidence:** Source IP: 203.0.113.10; Asset: auth-server-01; Events: login_failure, port_scan; Time range: 2026-10-13 09:54:00 to 2026-10-13 15:26:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services.

## Incident 5

- **Severity:** medium
- **Source IP:** 203.0.113.10
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:24:00
- **Last seen:** 2026-10-13 15:36:00
- **Event types:** file_access, login_failure, malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.10; Asset: web-server-01; Events: file_access, login_failure, malware_alert, unauthorized_access; Time range: 2026-10-13 08:24:00 to 2026-10-13 15:36:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 6

- **Severity:** medium
- **Source IP:** 203.0.113.10
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:33:00
- **Last seen:** 2026-10-13 12:46:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.10; Asset: workstation-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 09:33:00 to 2026-10-13 12:46:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 7

- **Severity:** high
- **Source IP:** 203.0.113.11
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 08:52:00
- **Last seen:** 2026-10-13 14:53:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.11; Asset: auth-server-01; Events: login_failure, malware_alert; Time range: 2026-10-13 08:52:00 to 2026-10-13 14:53:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 8

- **Severity:** medium
- **Source IP:** 203.0.113.11
- **Affected asset:** database-01
- **First seen:** 2026-10-13 10:17:00
- **Last seen:** 2026-10-13 13:43:00
- **Event types:** login_failure, malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.11; Asset: database-01; Events: login_failure, malware_alert, unauthorized_access; Time range: 2026-10-13 10:17:00 to 2026-10-13 13:43:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 9

- **Severity:** high
- **Source IP:** 203.0.113.11
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 12:05:00
- **Last seen:** 2026-10-13 13:22:00
- **Event types:** file_access, login_failure, privilege_escalation
- **Evidence:** Source IP: 203.0.113.11; Asset: web-server-01; Events: file_access, login_failure, privilege_escalation; Time range: 2026-10-13 12:05:00 to 2026-10-13 13:22:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** An attacker may gain elevated privileges. | Repeated failed logins may indicate an attempted account compromise. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity. | Verify whether the access was authorized and review relevant file permissions.

## Incident 10

- **Severity:** low
- **Source IP:** 203.0.113.11
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 10:45:00
- **Last seen:** 2026-10-13 13:00:00
- **Event types:** malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.11; Asset: workstation-01; Events: malware_alert, unauthorized_access; Time range: 2026-10-13 10:45:00 to 2026-10-13 13:00:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset.

## Incident 11

- **Severity:** medium
- **Source IP:** 203.0.113.12
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 10:51:00
- **Last seen:** 2026-10-13 12:42:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.12; Asset: auth-server-01; Events: login_failure, malware_alert; Time range: 2026-10-13 10:51:00 to 2026-10-13 12:42:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 12

- **Severity:** high
- **Source IP:** 203.0.113.12
- **Affected asset:** database-01
- **First seen:** 2026-10-13 09:13:00
- **Last seen:** 2026-10-13 15:46:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.12; Asset: database-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 09:13:00 to 2026-10-13 15:46:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 13

- **Severity:** high
- **Source IP:** 203.0.113.12
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:33:00
- **Last seen:** 2026-10-13 10:29:00
- **Event types:** file_access, login_success
- **Evidence:** Source IP: 203.0.113.12; Asset: web-server-01; Events: file_access, login_success; Time range: 2026-10-13 08:33:00 to 2026-10-13 10:29:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; Manual review required
- **Risk:** The event has no configured compliance mapping. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review the event and determine an appropriate control. | Verify whether the access was authorized and review relevant file permissions.

## Incident 14

- **Severity:** medium
- **Source IP:** 203.0.113.12
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:05:00
- **Last seen:** 2026-10-13 14:21:00
- **Event types:** malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.12; Asset: workstation-01; Events: malware_alert, unauthorized_access; Time range: 2026-10-13 09:05:00 to 2026-10-13 14:21:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset.

## Incident 15

- **Severity:** high
- **Source IP:** 203.0.113.13
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 08:18:00
- **Last seen:** 2026-10-13 15:35:00
- **Event types:** login_failure, login_success, malware_alert, privilege_escalation, unauthorized_access
- **Evidence:** Source IP: 203.0.113.13; Asset: auth-server-01; Events: login_failure, login_success, malware_alert, privilege_escalation, unauthorized_access; Time range: 2026-10-13 08:18:00 to 2026-10-13 15:35:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7; Manual review required
- **Risk:** An attacker may gain elevated privileges. | Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise. | The event has no configured compliance mapping. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity. | Review the event and determine an appropriate control.

## Incident 16

- **Severity:** critical
- **Source IP:** 203.0.113.13
- **Affected asset:** database-01
- **First seen:** 2026-10-13 13:27:00
- **Last seen:** 2026-10-13 13:27:00
- **Event types:** login_failure
- **Evidence:** Source IP: 203.0.113.13; Asset: database-01; Events: login_failure; Time range: 2026-10-13 13:27:00 to 2026-10-13 13:27:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 17

- **Severity:** critical
- **Source IP:** 203.0.113.13
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:04:00
- **Last seen:** 2026-10-13 08:04:00
- **Event types:** login_failure
- **Evidence:** Source IP: 203.0.113.13; Asset: web-server-01; Events: login_failure; Time range: 2026-10-13 08:04:00 to 2026-10-13 08:04:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 18

- **Severity:** high
- **Source IP:** 203.0.113.13
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 08:23:00
- **Last seen:** 2026-10-13 15:10:00
- **Event types:** login_failure, privilege_escalation, unauthorized_access
- **Evidence:** Source IP: 203.0.113.13; Asset: workstation-01; Events: login_failure, privilege_escalation, unauthorized_access; Time range: 2026-10-13 08:23:00 to 2026-10-13 15:10:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** An attacker may gain elevated privileges. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity.

## Incident 19

- **Severity:** low
- **Source IP:** 203.0.113.14
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 10:23:00
- **Last seen:** 2026-10-13 15:49:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.14; Asset: auth-server-01; Events: login_failure, malware_alert; Time range: 2026-10-13 10:23:00 to 2026-10-13 15:49:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 20

- **Severity:** low
- **Source IP:** 203.0.113.14
- **Affected asset:** database-01
- **First seen:** 2026-10-13 08:00:00
- **Last seen:** 2026-10-13 15:04:00
- **Event types:** file_access, login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.14; Asset: database-01; Events: file_access, login_failure, unauthorized_access; Time range: 2026-10-13 08:00:00 to 2026-10-13 15:04:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 21

- **Severity:** medium
- **Source IP:** 203.0.113.14
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:10:00
- **Last seen:** 2026-10-13 15:32:00
- **Event types:** file_access, login_failure, port_scan, privilege_escalation
- **Evidence:** Source IP: 203.0.113.14; Asset: web-server-01; Events: file_access, login_failure, port_scan, privilege_escalation; Time range: 2026-10-13 08:10:00 to 2026-10-13 15:32:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** An attacker may gain elevated privileges. | Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity. | Verify whether the access was authorized and review relevant file permissions.

## Incident 22

- **Severity:** low
- **Source IP:** 203.0.113.14
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:43:00
- **Last seen:** 2026-10-13 13:25:00
- **Event types:** file_access, login_failure, port_scan, unauthorized_access
- **Evidence:** Source IP: 203.0.113.14; Asset: workstation-01; Events: file_access, login_failure, port_scan, unauthorized_access; Time range: 2026-10-13 09:43:00 to 2026-10-13 13:25:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services. | Verify whether the access was authorized and review relevant file permissions.

## Incident 23

- **Severity:** high
- **Source IP:** 203.0.113.15
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 09:59:00
- **Last seen:** 2026-10-13 13:45:00
- **Event types:** login_failure, port_scan
- **Evidence:** Source IP: 203.0.113.15; Asset: auth-server-01; Events: login_failure, port_scan; Time range: 2026-10-13 09:59:00 to 2026-10-13 13:45:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services.

## Incident 24

- **Severity:** medium
- **Source IP:** 203.0.113.15
- **Affected asset:** database-01
- **First seen:** 2026-10-13 10:35:00
- **Last seen:** 2026-10-13 14:40:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.15; Asset: database-01; Events: login_failure, malware_alert; Time range: 2026-10-13 10:35:00 to 2026-10-13 14:40:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 25

- **Severity:** medium
- **Source IP:** 203.0.113.15
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 09:41:00
- **Last seen:** 2026-10-13 11:16:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.15; Asset: web-server-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 09:41:00 to 2026-10-13 11:16:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 26

- **Severity:** high
- **Source IP:** 203.0.113.15
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:10:00
- **Last seen:** 2026-10-13 09:10:00
- **Event types:** unauthorized_access
- **Evidence:** Source IP: 203.0.113.15; Asset: workstation-01; Events: unauthorized_access; Time range: 2026-10-13 09:10:00 to 2026-10-13 09:10:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3
- **Risk:** Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset.

## Incident 27

- **Severity:** critical
- **Source IP:** 203.0.113.2
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 10:04:00
- **Last seen:** 2026-10-13 10:04:00
- **Event types:** port_scan
- **Evidence:** Source IP: 203.0.113.2; Asset: auth-server-01; Events: port_scan; Time range: 2026-10-13 10:04:00 to 2026-10-13 10:04:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services.
- **Recommended remediation:** Review network logs and restrict unnecessary exposed services.

## Incident 28

- **Severity:** high
- **Source IP:** 203.0.113.2
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 09:07:00
- **Last seen:** 2026-10-13 14:09:00
- **Event types:** file_access, login_failure, login_success, malware_alert
- **Evidence:** Source IP: 203.0.113.2; Asset: web-server-01; Events: file_access, login_failure, login_success, malware_alert; Time range: 2026-10-13 09:07:00 to 2026-10-13 14:09:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7; Manual review required
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise. | The event has no configured compliance mapping. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review the event and determine an appropriate control. | Verify whether the access was authorized and review relevant file permissions.

## Incident 29

- **Severity:** high
- **Source IP:** 203.0.113.2
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:19:00
- **Last seen:** 2026-10-13 15:44:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.2; Asset: workstation-01; Events: login_failure, malware_alert; Time range: 2026-10-13 09:19:00 to 2026-10-13 15:44:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 30

- **Severity:** high
- **Source IP:** 203.0.113.3
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 09:16:00
- **Last seen:** 2026-10-13 12:14:00
- **Event types:** malware_alert, port_scan
- **Evidence:** Source IP: 203.0.113.3; Asset: auth-server-01; Events: malware_alert, port_scan; Time range: 2026-10-13 09:16:00 to 2026-10-13 12:14:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Port scanning may indicate reconnaissance for vulnerable services.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review network logs and restrict unnecessary exposed services.

## Incident 31

- **Severity:** medium
- **Source IP:** 203.0.113.3
- **Affected asset:** database-01
- **First seen:** 2026-10-13 08:30:00
- **Last seen:** 2026-10-13 10:49:00
- **Event types:** login_failure, privilege_escalation
- **Evidence:** Source IP: 203.0.113.3; Asset: database-01; Events: login_failure, privilege_escalation; Time range: 2026-10-13 08:30:00 to 2026-10-13 10:49:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.5
- **Risk:** An attacker may gain elevated privileges. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity.

## Incident 32

- **Severity:** low
- **Source IP:** 203.0.113.3
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:42:00
- **Last seen:** 2026-10-13 15:40:00
- **Event types:** malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.3; Asset: web-server-01; Events: malware_alert, unauthorized_access; Time range: 2026-10-13 08:42:00 to 2026-10-13 15:40:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset.

## Incident 33

- **Severity:** critical
- **Source IP:** 203.0.113.3
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 12:07:00
- **Last seen:** 2026-10-13 14:55:00
- **Event types:** port_scan, unauthorized_access
- **Evidence:** Source IP: 203.0.113.3; Asset: workstation-01; Events: port_scan, unauthorized_access; Time range: 2026-10-13 12:07:00 to 2026-10-13 14:55:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review network logs and restrict unnecessary exposed services.

## Incident 34

- **Severity:** high
- **Source IP:** 203.0.113.4
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 13:16:00
- **Last seen:** 2026-10-13 14:14:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.4; Asset: auth-server-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 13:16:00 to 2026-10-13 14:14:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 35

- **Severity:** medium
- **Source IP:** 203.0.113.4
- **Affected asset:** database-01
- **First seen:** 2026-10-13 08:16:00
- **Last seen:** 2026-10-13 08:54:00
- **Event types:** login_failure, privilege_escalation
- **Evidence:** Source IP: 203.0.113.4; Asset: database-01; Events: login_failure, privilege_escalation; Time range: 2026-10-13 08:16:00 to 2026-10-13 08:54:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.5
- **Risk:** An attacker may gain elevated privileges. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity.

## Incident 36

- **Severity:** medium
- **Source IP:** 203.0.113.4
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 08:58:00
- **Last seen:** 2026-10-13 14:34:00
- **Event types:** file_access, login_failure, port_scan, unauthorized_access
- **Evidence:** Source IP: 203.0.113.4; Asset: web-server-01; Events: file_access, login_failure, port_scan, unauthorized_access; Time range: 2026-10-13 08:58:00 to 2026-10-13 14:34:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services. | Verify whether the access was authorized and review relevant file permissions.

## Incident 37

- **Severity:** medium
- **Source IP:** 203.0.113.4
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 10:40:00
- **Last seen:** 2026-10-13 15:53:00
- **Event types:** login_success, unauthorized_access
- **Evidence:** Source IP: 203.0.113.4; Asset: workstation-01; Events: login_success, unauthorized_access; Time range: 2026-10-13 10:40:00 to 2026-10-13 15:53:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; Manual review required
- **Risk:** The event has no configured compliance mapping. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review the event and determine an appropriate control.

## Incident 38

- **Severity:** medium
- **Source IP:** 203.0.113.5
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 08:27:00
- **Last seen:** 2026-10-13 08:27:00
- **Event types:** file_access
- **Evidence:** Source IP: 203.0.113.5; Asset: auth-server-01; Events: file_access; Time range: 2026-10-13 08:27:00 to 2026-10-13 08:27:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3
- **Risk:** Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Verify whether the access was authorized and review relevant file permissions.

## Incident 39

- **Severity:** medium
- **Source IP:** 203.0.113.5
- **Affected asset:** database-01
- **First seen:** 2026-10-13 10:25:00
- **Last seen:** 2026-10-13 14:02:00
- **Event types:** file_access, login_failure
- **Evidence:** Source IP: 203.0.113.5; Asset: database-01; Events: file_access, login_failure; Time range: 2026-10-13 10:25:00 to 2026-10-13 14:02:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 40

- **Severity:** medium
- **Source IP:** 203.0.113.5
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 10:19:00
- **Last seen:** 2026-10-13 15:02:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.5; Asset: web-server-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 10:19:00 to 2026-10-13 15:02:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 41

- **Severity:** medium
- **Source IP:** 203.0.113.5
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 13:57:00
- **Last seen:** 2026-10-13 13:57:00
- **Event types:** file_access
- **Evidence:** Source IP: 203.0.113.5; Asset: workstation-01; Events: file_access; Time range: 2026-10-13 13:57:00 to 2026-10-13 13:57:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3
- **Risk:** Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Verify whether the access was authorized and review relevant file permissions.

## Incident 42

- **Severity:** medium
- **Source IP:** 203.0.113.6
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 08:08:00
- **Last seen:** 2026-10-13 15:59:00
- **Event types:** file_access, login_failure
- **Evidence:** Source IP: 203.0.113.6; Asset: auth-server-01; Events: file_access, login_failure; Time range: 2026-10-13 08:08:00 to 2026-10-13 15:59:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 43

- **Severity:** medium
- **Source IP:** 203.0.113.6
- **Affected asset:** database-01
- **First seen:** 2026-10-13 10:00:00
- **Last seen:** 2026-10-13 12:59:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.6; Asset: database-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 10:00:00 to 2026-10-13 12:59:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 44

- **Severity:** high
- **Source IP:** 203.0.113.6
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 14:24:00
- **Last seen:** 2026-10-13 15:55:00
- **Event types:** login_failure, port_scan
- **Evidence:** Source IP: 203.0.113.6; Asset: web-server-01; Events: login_failure, port_scan; Time range: 2026-10-13 14:24:00 to 2026-10-13 15:55:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services.

## Incident 45

- **Severity:** medium
- **Source IP:** 203.0.113.6
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 08:41:00
- **Last seen:** 2026-10-13 15:20:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.6; Asset: workstation-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 08:41:00 to 2026-10-13 15:20:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 46

- **Severity:** medium
- **Source IP:** 203.0.113.7
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 08:36:00
- **Last seen:** 2026-10-13 15:06:00
- **Event types:** file_access, login_failure, port_scan, unauthorized_access
- **Evidence:** Source IP: 203.0.113.7; Asset: auth-server-01; Events: file_access, login_failure, port_scan, unauthorized_access; Time range: 2026-10-13 08:36:00 to 2026-10-13 15:06:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services. | Verify whether the access was authorized and review relevant file permissions.

## Incident 47

- **Severity:** low
- **Source IP:** 203.0.113.7
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 11:21:00
- **Last seen:** 2026-10-13 13:41:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.7; Asset: web-server-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 11:21:00 to 2026-10-13 13:41:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 48

- **Severity:** medium
- **Source IP:** 203.0.113.7
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 13:11:00
- **Last seen:** 2026-10-13 14:45:00
- **Event types:** file_access, malware_alert, unauthorized_access
- **Evidence:** Source IP: 203.0.113.7; Asset: workstation-01; Events: file_access, malware_alert, unauthorized_access; Time range: 2026-10-13 13:11:00 to 2026-10-13 14:45:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review access permissions and investigate the affected account and asset. | Verify whether the access was authorized and review relevant file permissions.

## Incident 49

- **Severity:** high
- **Source IP:** 203.0.113.8
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 12:23:00
- **Last seen:** 2026-10-13 13:34:00
- **Event types:** file_access, malware_alert
- **Evidence:** Source IP: 203.0.113.8; Asset: auth-server-01; Events: file_access, malware_alert; Time range: 2026-10-13 12:23:00 to 2026-10-13 13:34:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Verify whether the access was authorized and review relevant file permissions.

## Incident 50

- **Severity:** critical
- **Source IP:** 203.0.113.8
- **Affected asset:** database-01
- **First seen:** 2026-10-13 13:14:00
- **Last seen:** 2026-10-13 13:14:00
- **Event types:** file_access
- **Evidence:** Source IP: 203.0.113.8; Asset: database-01; Events: file_access; Time range: 2026-10-13 13:14:00 to 2026-10-13 13:14:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3
- **Risk:** Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Verify whether the access was authorized and review relevant file permissions.

## Incident 51

- **Severity:** high
- **Source IP:** 203.0.113.8
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 09:46:00
- **Last seen:** 2026-10-13 15:17:00
- **Event types:** file_access, login_failure
- **Evidence:** Source IP: 203.0.113.8; Asset: web-server-01; Events: file_access, login_failure; Time range: 2026-10-13 09:46:00 to 2026-10-13 15:17:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Verify whether the access was authorized and review relevant file permissions.

## Incident 52

- **Severity:** low
- **Source IP:** 203.0.113.8
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 08:46:00
- **Last seen:** 2026-10-13 13:20:00
- **Event types:** login_failure, unauthorized_access
- **Evidence:** Source IP: 203.0.113.8; Asset: workstation-01; Events: login_failure, unauthorized_access; Time range: 2026-10-13 08:46:00 to 2026-10-13 13:20:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.3; ISO 27001:2022 Annex A 8.5
- **Risk:** Repeated failed logins may indicate an attempted account compromise. | Unauthorized access may expose sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

## Incident 53

- **Severity:** low
- **Source IP:** 203.0.113.9
- **Affected asset:** auth-server-01
- **First seen:** 2026-10-13 09:49:00
- **Last seen:** 2026-10-13 10:57:00
- **Event types:** login_failure, port_scan
- **Evidence:** Source IP: 203.0.113.9; Asset: auth-server-01; Events: login_failure, port_scan; Time range: 2026-10-13 09:49:00 to 2026-10-13 10:57:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.5
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Review authentication logs, enforce MFA, and apply appropriate login rate limits. | Review network logs and restrict unnecessary exposed services.

## Incident 54

- **Severity:** high
- **Source IP:** 203.0.113.9
- **Affected asset:** database-01
- **First seen:** 2026-10-13 10:06:00
- **Last seen:** 2026-10-13 11:56:00
- **Event types:** malware_alert, port_scan, privilege_escalation
- **Evidence:** Source IP: 203.0.113.9; Asset: database-01; Events: malware_alert, port_scan, privilege_escalation; Time range: 2026-10-13 10:06:00 to 2026-10-13 11:56:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.2; ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.7
- **Risk:** An attacker may gain elevated privileges. | Malware may compromise systems or data. | Port scanning may indicate reconnaissance for vulnerable services.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review network logs and restrict unnecessary exposed services. | Review privileged accounts, revoke unauthorized permissions, and investigate the activity.

## Incident 55

- **Severity:** medium
- **Source IP:** 203.0.113.9
- **Affected asset:** web-server-01
- **First seen:** 2026-10-13 09:22:00
- **Last seen:** 2026-10-13 14:43:00
- **Event types:** file_access, port_scan, unauthorized_access
- **Evidence:** Source IP: 203.0.113.9; Asset: web-server-01; Events: file_access, port_scan, unauthorized_access; Time range: 2026-10-13 09:22:00 to 2026-10-13 14:43:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.20; ISO 27001:2022 Annex A 8.3
- **Risk:** Port scanning may indicate reconnaissance for vulnerable services. | Unauthorized access may expose sensitive information. | Unexpected file access may expose or modify sensitive information.
- **Recommended remediation:** Review access permissions and investigate the affected account and asset. | Review network logs and restrict unnecessary exposed services. | Verify whether the access was authorized and review relevant file permissions.

## Incident 56

- **Severity:** high
- **Source IP:** 203.0.113.9
- **Affected asset:** workstation-01
- **First seen:** 2026-10-13 09:29:00
- **Last seen:** 2026-10-13 14:32:00
- **Event types:** login_failure, malware_alert
- **Evidence:** Source IP: 203.0.113.9; Asset: workstation-01; Events: login_failure, malware_alert; Time range: 2026-10-13 09:29:00 to 2026-10-13 14:32:00
- **Compliance controls:** ISO 27001:2022 Annex A 8.5; ISO 27001:2022 Annex A 8.7
- **Risk:** Malware may compromise systems or data. | Repeated failed logins may indicate an attempted account compromise.
- **Recommended remediation:** Investigate the alert, isolate the affected system if warranted, and run approved security scans. | Review authentication logs, enforce MFA, and apply appropriate login rate limits.

