def format_response(result):
    output = f"""
Incident Type: {result['incident_type']}
Severity: {result['severity']}
MITRE: {result['mitre']}

Entities:
- IPs: {', '.join(result['entities']['ips']) or 'None'}
- Users: {', '.join(result['entities']['users']) or 'None'}

Playbook Steps:
"""

    for i, step in enumerate(result["playbook"]["steps"], 1):
        output += f"{i}. {step}\n"

    return output