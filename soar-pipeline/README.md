# SOAR Pipeline

This project implements a Security Orchestration, Automation, and Response (SOAR) pipeline that ingests alerts, enriches Indicators of Compromise (IOCs), triages them, simulates device isolation, and outputs a normalized incident JSON along with a Jinja2 Markdown analyst summary.

## Project Structure

```
soar-pipeline
├── src
│   ├── __init__.py
│   ├── ingest.py
│   ├── enrich.py
│   ├── triage.py
│   ├── isolate.py
│   ├── normalize.py
│   ├── summary.py
│   └── templates
│       └── analyst_summary.md.j2
├── requirements.txt
├── setup.py
└── README.md
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd soar-pipeline
pip install -r requirements.txt
```

## Usage

1. **Ingest Alerts**: Use the `ingest_alert(file_path)` function from `src/ingest.py` to read a JSON alert file and return the alert data in a normalized format.
   
2. **Enrich IOCs**: Call `enrich_iocs(iocs)` from `src/enrich.py` to enrich a list of IOCs using local mock threat intelligence data.

3. **Triage Alerts**: Evaluate the severity of alerts using `triage_alert(alert)` from `src/triage.py`, which applies allowlist suppression and tags alerts with MITRE ATT&CK techniques.

4. **Simulate Device Isolation**: Use `simulate_isolation(device_id, incident_id)` from `src/isolate.py` to log device isolation actions based on alert criteria.

5. **Normalize Alerts**: Transform alerts into a normalized structure with `normalize_alert(alert)` from `src/normalize.py`.

6. **Generate Summary**: Create a Markdown summary of the incident using `generate_summary(incident)` from `src/summary.py`, which utilizes Jinja2 for rendering.

## Testing

To test the functionality of the pipeline, you can create unit tests for each module in the `src` directory. Ensure that all tests pass before deploying the pipeline.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.