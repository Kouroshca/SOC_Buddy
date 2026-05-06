import streamlit as st
from main import generate_response

st.title("Welcome to SOC Buddy")

user_input = st.text_area("Paste your alert/log")

if st.button("Analyze"):
    result = generate_response(user_input)

    st.subheader("Incident Type")
    st.write(result["incident_type"])

    st.subheader("Severity")
    st.write(result["severity"])

    st.subheader("MITRE ATT&CK")
    st.write(result["mitre"])

    st.subheader("Entities Extracted")
    st.write(result["entities"])

    st.subheader("Playbook")
    for step in result["playbook"]["steps"]:
        st.write("- ", step)