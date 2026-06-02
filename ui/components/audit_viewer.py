import streamlit as st
from db.db_manager import fetch_all_events

def show_audit_logs():
    st.header("📊 Audit Logs")

    events = fetch_all_events()

    for event in events:
        with st.expander(f"Event ID: {event[0]} | {event[3]}"):
            st.write(f"Equipment: {event[2]}")
            st.write(f"Issue: {event[3]}")
            st.write(f"Confidence: {event[4]}")
            st.write(f"Timestamp: {event[1]}")