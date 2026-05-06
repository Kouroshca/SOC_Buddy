def get_severity(incident_type):
    mapping = {
        "brute_force": "High",
        "phishing": "Medium",
        "malware": "High",
        "unknown": "Low"
    }
    return mapping.get(incident_type, "Low")


def get_mitre_mapping(incident_type):
    mitre_map = {
        "brute_force": "T1110 - Brute Force",
        "phishing": "T1566 - Phishing",
        "malware": "T1204 - User Execution"
    }
    return mitre_map.get(incident_type, "N/A")