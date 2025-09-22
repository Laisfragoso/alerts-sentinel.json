def normalize_alert(alert):
    normalized_alert = {
        "original_alert": alert,
        "indicators": alert.get("indicators", [])
    }
    return normalized_alert