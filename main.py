import json

with open("playbooks.json") as f:
    playbooks = json,load(f)

def get_playbook(incident_type):
    """Retrieves the playbook. If not found, returns a default message."""
    return playbooks.get(incident_type, {
        "title": "Unknown Incident",
        "steps": ["Alert supervisor", "Perform manual investigation"]
    })