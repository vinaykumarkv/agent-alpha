import streamlit as st
from services.pipeline import run_pipeline
from db.db_manager import fetch_all_events
from ui.components.dashboard import show_results, show_metrics
from ui.components.uploader import upload_image
from ui.components.dashboard import show_results
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
        if st.button("🔍 Analyze"):
            with st.spinner("Running AI pipeline..."):
                result = run_pipeline(image_path)

            st.session_state["last_result"] = result

    # ✅ Show results if available
    if "last_result" in st.session_state:
        show_results(st.session_state["last_result"])
        show_feedback(st.session_state["last_result"]["event_id"])


# =========================
# 📊 DASHBOARD TAB (KPI)
# =========================
with tab2:
    st.header("📊 System Performance Dashboard")

    events = fetch_all_events()

    if events:
        df = pd.DataFrame(events, columns=[
            "id", "timestamp", "equipment", "issue", "confidence", "image", "telemetry"
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

with tab3:
    st.header("📊 System Metrics")

    # ✅ Mock metrics for demonstration
    metrics = {
        "latency_sec": round(st.session_state.get("last_result", {}).get("final_output", {}).get("confidence_level", 0) * 5, 2),
        "tokens_used": st.session_state.get("last_result", {}).get("diagnostics", {}).get("risk_level", 0) * 100,
        "cpu_usage": round(st.session_state.get("last_result", {}).get("diagnostics", {}).get("risk_level", 0) * 80, 2),
        "memory_usage": round(st.session_state.get("last_result", {}).get("diagnostics", {}).get("risk_level", 0) * 70, 2)
    }

    show_metrics(metrics)
# =========================
# 🗄️ AUDIT LOGS TAB
# =========================
with tab4:
    show_audit_logs()