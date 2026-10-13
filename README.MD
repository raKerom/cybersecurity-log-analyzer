# Cybersecurity Log Analyzer

A Python-based cybersecurity log analysis prototype that uses machine learning to identify suspicious security events, correlate potential incidents, map findings to ISO 27001 controls, and generate security reports.

## Overview

The Cybersecurity Log Analyzer demonstrates a basic security-event analysis pipeline using a synthetic dataset. It combines a Decision Tree classifier with rule-based alert correlation and compliance mapping.

## Features

- **Log preprocessing:** Handles timestamps, missing values, duplicates, and labels.
- **Machine learning:** Trains a Decision Tree classifier to classify logs as Normal or Suspicious.
- **Alert correlation:** Groups suspicious events by source IP address and affected asset.
- **Compliance mapping:** Maps selected event types to proposed ISO 27001:2022 Annex A controls.
- **Security reporting:** Generates CSV and Markdown reports containing potential incidents and remediation suggestions.
- **REST API:** Provides a FastAPI endpoint for analyzing submitted security logs.

## Tech Stack

- Python
- Pandas
- Scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- Joblib

## Project Structure

```text
cybersecurity-log-analyzer/
├── api.py
├── pre_process.py
├── train_model.py
├── correlate_alerts.py
├── compliance_mapping.py
├── generate_report.py
├── security_logs.csv
├── processed_logs.csv
├── security_model.pkl
├── correlated_incidents.csv
├── security_report.csv
├── security_report.md
├── requirements.txt
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/raKerom/cybersecurity-log-analyzer.git
cd cybersecurity-log-analyzer
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the analysis pipeline

Run these scripts from the project root:

```bash
python pre_process.py
python train_model.py
python correlate_alerts.py
python generate_report.py
```

The scripts generate processed logs, a trained model, correlated incident data, and security reports.

### 5. Start the API

```bash
uvicorn api:app --reload
```

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

Use the documentation to test the available endpoint with sample security-log data.

## Machine Learning Evaluation

The Decision Tree classifier was evaluated on a held-out test set.

| Metric | Normal | Suspicious |
|---|---:|---:|
| Precision | 0.96 | 0.97 |
| Recall | 0.98 | 0.94 |
| F1-score | 0.97 | 0.95 |

**Overall accuracy: 96.3%**

These results reflect performance on the project's synthetic dataset and should not be interpreted as evidence of equivalent performance on real-world security logs.

## Alert Correlation

Suspicious events are grouped using source IP addresses and affected assets. The resulting incident data includes event counts, event types, timestamps, and severity information.

The correlation logic is a prototype and does not provide comprehensive, production-grade incident correlation.

## Compliance Mapping

The project includes proposed mappings between selected security event types and ISO 27001:2022 Annex A controls, alongside risk descriptions and remediation suggestions.

These mappings are illustrative and should be validated against the organization's security policies and compliance requirements before practical use.

## Limitations

- The included dataset is synthetic and may not represent real cybersecurity activity.
- Model evaluation results may be inflated by patterns built into the generated data.
- Alert correlation is rule-based and limited in scope.
- The API correlates events submitted in the same request; it does not maintain a persistent incident history across requests.
- The project does not currently provide a production-grade external security-data connector.
- Compliance mappings are proposed references, not proof of a compliance violation.

## Future Improvements

- Integrate a real security-log source or threat-intelligence API.
- Improve time-window-based alert correlation.
- Evaluate the model on representative real-world datasets.
- Add automated tests, authentication, and stronger API error handling.
- Expand compliance mapping validation.

## Disclaimer

This project was developed as an educational prototype to demonstrate basic machine learning, security-log analysis, API development, and compliance-mapping concepts. It is not intended to replace a production Security Information and Event Management (SIEM) platform.

## Author

**Raj Morekar**

GitHub: https://github.com/raKerom