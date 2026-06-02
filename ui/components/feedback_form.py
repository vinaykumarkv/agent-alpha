import streamlit as st
from db.db_manager import log_feedback

def show_feedback(event_id):
    st.subheader("✅ Provide Feedback")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👍 Correct"):
            log_feedback(
                event_id,
                True,
                "AI correct",
                "As suggested",
                10
            )
            st.success("Feedback recorded")

    with col2:
        if st.button("👎 Incorrect"):
            log_feedback(
                event_id,
                False,
                "AI incorrect",
                "Manual correction",
                20
            )
            st.warning("Feedback recorded")