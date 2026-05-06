from classificator import enhanced_classifier
from parser_1 import extract_entities
from enrichment import get_severity, get_mitre_mapping
import json


with open("Playbooks/Playbooks.json") as f:
    playbooks = json.load(f)

def get_playbook(incident_type):
    return playbooks.get(incident_type, {"title": "Unknown", "steps": ["Investigate manually"]})


def generate_response(text):
    incident = enhanced_classifier(text)
    entities = extract_entities(text)

    playbook = get_playbook(incident)

    severity = get_severity(incident)
    mitre = get_mitre_mapping(incident)

    return {
        "incident_type": incident,
        "entities": entities,
        "severity": severity,
        "mitre": mitre,
        "playbook": playbook
    }