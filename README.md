# SOC_Buddy

** SOC Buddy:

SOC Playbook Assistant is a Python-based security tool that helps analysts quickly respond to incidents by transforming raw alerts and logs into structured, actionable response playbooks.
It simulates a real Security Operations Center (SOC) workflow by classifying threats, extracting key indicators, and providing step-by-step remediation guidance.

🚀 Live Demo -> (https://socbuddy.streamlit.app)
🎥 YouTube Demo -> 
📌 Features:

  🔍 Incident Classification
  Detects common threats such as brute force, phishing, malware, and privilege escalation
  🧩 Entity Extraction
  Parses unstructured logs to extract key indicators like IP addresses and usernames
  ⚠️ Severity Scoring

  Assigns Low / Medium / High severity levels based on incident type
  🛡 MITRE ATT&CK Mapping
    Maps incidents to relevant techniques (e.g., T1110 – Brute Force)
  📋 Automated Playbooks
    Generates structured, step-by-step response actions for SOC analysts
  💻 Interactive UI
    Streamlit-based interface for real-time analysis and response generation
  🧠 How It Works
  User inputs a security alert or log
  System classifies the incident type
  Extracts entities such as IPs and usernames
  Assigns severity and maps to MITRE ATT&CK
  Returns a detailed response playbook
🛠 Tech Stack
Python
Streamlit
JSON (playbook storage)
Regex (log parsing)

📌 Author
Kourosh Kalatian
Aspiring SOC Analyst | Python Developer
