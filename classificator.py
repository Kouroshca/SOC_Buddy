SIGNATURES = {
    "brute_force": ["failed login", "unauthorized access", "ssh", "port 22"],
    "phishing": ["email", "link", "bank", "verify account", "urgent"],
    "malware": ["quarantine", "exe", "malicious", "c2 server"],
    "privilege_escalation": ["root", "escalate", "unusual sudo", "shadow file"]
}

def enhanced_classifier(text):
    text = text.lower()
    for incident_type, keywords in SIGNATURES.items():
        if any(keyword in text for keyword in keywords):
            return incident_type
        
    return "general_investigation"
