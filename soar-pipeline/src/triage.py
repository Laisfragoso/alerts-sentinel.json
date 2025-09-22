def triage_alert(alert):
    severity_rules = {
        'high': ['malware', 'data_exfiltration', 'ransomware'],
        'medium': ['phishing', 'brute_force'],
        'low': ['information_gathering', 'reconnaissance']
    }

    allowlist = ['trusted_source@example.com', 'internal_ip_range']

    # Check if the alert is from an allowlisted source
    if alert['source'] in allowlist:
        alert['status'] = 'suppressed'
        return alert

    # Evaluate severity based on predefined rules
    for severity, keywords in severity_rules.items():
        if any(keyword in alert['description'] for keyword in keywords):
            alert['severity'] = severity
            break
    else:
        alert['severity'] = 'unknown'

    # Tag the alert with MITRE ATT&CK techniques
    mitre_techniques = {
        'malware': 'T1203',
        'data_exfiltration': 'T1041',
        'ransomware': 'T1486',
        'phishing': 'T1566',
        'brute_force': 'T1110',
        'information_gathering': 'T1598',
        'reconnaissance': 'T1595'
    }

    alert['tags'] = [mitre_techniques.get(keyword) for keyword in severity_rules['high'] if keyword in alert['description']]

    return alert