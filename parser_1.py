import re

def extract_entities(text):
    ip_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    user_pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

    ips = re.findall(ip_pattern, text)
    users = re.findall(user_pattern, text, re.IGNORECASE)

    return {
    "ips": list(set(ips)),
    "users": list(set(users))
}