import streamlit as st
from services.pipeline import run_pipeline

from ui.components.uploader import upload_image
from ui.components.dashboard import show_results
from ui.components.feedback_form import show_feedback
from ui.components.audit_viewer import show_audit_logs

st.set_page_config(page_title="AI Copilot", layout="wide")

st.title("🧠 Multimodal Field Service Copilot")

menu = st.sidebar.selectbox("Menu", ["Run Analysis", "Audit Logs"])

# =========================
# RUN ANALYSIS
# =========================
if menu == "Run Analysis":

    st.header("📸 Upload Equipment Image")

    image_path = upload_image()

    if image_path:
        if st.button("🔍 Analyze"):
            with st.spinner("Running AI pipeline..."):
                result = run_pipeline(image_path)

            # ✅ Show results
            show_results(result)

            # ✅ Feedback
            show_feedback(result["event_id"])

# =========================
# AUDIT LOGS
# =========================
elif menu == "Audit Logs":
    show_audit_logs()
