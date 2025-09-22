def ingest_alert(file_path):
    import json

    with open(file_path, 'r') as file:
        alert_data = json.load(file)

    normalized_alert = {
        "original_alert": alert_data,
        "indicators": alert_data.get("indicators", [])
    }

    return normalized_alert