import sys
import os
from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from services.pipeline import run_pipeline
from db.db_manager import fetch_all_events
from ui.components.dashboard import show_results, show_metrics
from ui.components.uploader import upload_image
from ui.components.feedback_form import show_feedback
from ui.components.audit_viewer import show_audit_logs

import pandas as pd

st.set_page_config(page_title="AI Copilot", layout="wide")

st.title("🧠 Multimodal Field Service Copilot")

# ✅ Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📊 Dashboard", "⚙️ System Metrics", "🗄️ Audit Logs"])

# =========================
# 🏠 HOME TAB (ANALYSIS)
# =========================
with tab1:
    st.header("📸 Upload Equipment Image")

    image_path = upload_image()

    if image_path:
        # ✅ Clean separation: The button ONLY triggers the pipeline run and updates state
        if st.button("🔍 Analyze"):
            with st.spinner("Running AI pipeline..."):
                result = run_pipeline(image_path)
            st.session_state["last_result"] = result

    # ✅ FIXED: Kept outside of the button check block.
    # Now, if someone submits feedback, the results won't disappear!
    if "last_result" in st.session_state:
        show_results(st.session_state["last_result"])
        
        # Safely fetch event_id using .get() to prevent hard crashes if key missing
        event_id = st.session_state["last_result"].get("event_id")
        if event_id:
            show_feedback(event_id)


# =========================
# 📊 DASHBOARD TAB (KPI)
# =========================
with tab2:
    st.header("📊 System Performance Dashboard")

    events = fetch_all_events()

    if events:
        df = pd.DataFrame(events, columns=[
            "id", "timestamp", "equipment", "issue", "confidence", "image", "telemetry","metrics","None"
        ])

        # ✅ Metrics
        st.metric("Total Events", len(df))
        st.metric("Avg Confidence", round(df["confidence"].mean(), 2))

        # ✅ Issue distribution
        st.subheader("📌 Issue Distribution")
        st.bar_chart(df["issue"].value_counts())

        # ✅ Equipment distribution
        st.subheader("🏭 Equipment Distribution")
        st.bar_chart(df["equipment"].value_counts())

        # 🔁 Trend over time (confidence)
        st.subheader("📈 Confidence Trend")
        st.line_chart(df["confidence"])

        # 🔁 Events over time
        st.subheader("📊 Events Over Time")
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df_grouped = df.groupby(df["timestamp"].dt.date).size()
        st.line_chart(df_grouped)

    else:
        st.info("No data available yet. Run analysis first.")

# =========================
# ⚙️ SYSTEM METRICS TAB
# =========================
with tab3:
    st.header("📊 System Metrics")

    last_result = st.session_state.get("last_result", {})
    metrics = last_result.get("metrics", {})
    final_output = last_result.get("final_output", {})
    diagnostics = last_result.get("diagnostics", {})

    # --- SAFE DATATYPE CONVERSION ---
    # Fetch raw value
    raw_confidence = final_output.get("confidence_level", 0)
    
    # Try converting to a float in case it's a string like "0.95"
    try:
        confidence_num = float(raw_confidence)
    except (ValueError, TypeError):
        # Fallback default value if the text cannot be converted to a number
        confidence_num = 0.0

    metrics = {
        "latency_sec": metrics.get("latency_sec", 0),
        "tokens_used": metrics.get("tokens_used", 0),
        "cpu_usage": metrics.get("cpu_usage", 0),
        "memory_usage": metrics.get("memory_usage", 0),
        "confidence_level": confidence_num,
    }

    show_metrics(metrics)


# =========================
# 🗄️ AUDIT LOGS TAB
# =========================
with tab4:
    show_audit_logs()
