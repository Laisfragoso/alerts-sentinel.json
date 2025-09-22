def enrich_iocs(iocs):
    enriched_iocs = []
    threat_intel_data = load_threat_intelligence_data()

    for ioc in iocs:
        enrichment = {
            "ioc": ioc,
            "threat_level": "unknown",
            "description": "No description available"
        }

        if ioc in threat_intel_data:
            enrichment.update(threat_intel_data[ioc])

        enriched_iocs.append(enrichment)

    return enriched_iocs

def load_threat_intelligence_data():
    # Mock threat intelligence data
    return {
        "malicious.com": {
            "threat_level": "high",
            "description": "Known phishing domain"
        },
        "suspicious.net": {
            "threat_level": "medium",
            "description": "Potentially harmful site"
        }
    }