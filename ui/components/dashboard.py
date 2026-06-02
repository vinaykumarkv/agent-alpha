# ui/components/dashboard.py
import streamlit as st
from db.db_manager import fetch_feedback

def show_results(result):
    st.subheader("🔎 Detection")
    st.json(result["vision"])

    st.subheader("🧠 Diagnostics")
    st.json(result["diagnostics"])

    # Safely fetch numeric risk level fallback to 0
    risk_level = result.get("diagnostics", {}).get("risk_level", 0)
    st.metric("⚠️ Risk Level", risk_level)

    st.subheader("📚 Knowledge Retrieved")
    knowledge_docs = result.get("knowledge", {}).get("documents", [])
    if knowledge_docs:
        st.write(knowledge_docs[0])
    else:
        st.info("No knowledge documents were retrieved.")

    st.subheader("🛠️ Recommended Steps")
    final_steps = result.get("final_output", {}).get("final_steps", [])
    for step in final_steps:
        st.write(f"- {step}")

    st.subheader("📖 Explanation")
    st.write(result.get("final_output", {}).get("explanation", ""))

    st.success(f"Confidence: {result.get('final_output', {}).get('confidence_level', 0)}")
    
    # --- SAFE DATABASE CALCULATIONS ---
    feedback_data = fetch_feedback()

    if feedback_data:
        total = len(feedback_data)
        # Prevent indexing issues by handling standard database rows safely
        try:
            correct = sum(1 for f in feedback_data if len(f) > 0 and f[0] == 1)
            accuracy = round((correct / total) * 100, 2)
            st.metric("✅ AI Accuracy (%)", accuracy)
            
            # Change indexing if resolution time is stored in a different column (e.g., column index 4)
            times = [f[4] for f in feedback_data if len(f) > 4 and f[4] is not None]
            if times:
                avg_time = sum(times) / len(times)
                st.metric("⏱ Avg Resolution Time", round(avg_time, 2))
        except Exception as e:
            st.error(f"Error displaying feedback metrics: {e}")

def show_metrics(metrics):
    st.subheader("⚙️ System Metrics")
    col1, col2, col3 = st.columns(3)

    col1.metric("⏱ Latency (sec)", metrics.get("latency_sec", 0))
    col2.metric("🧠 Tokens Used", metrics.get("tokens_used", 0))
    col3.metric("🖥 CPU Usage (%)", metrics.get("cpu_usage", 0))

    st.metric("💾 Memory Usage (%)", metrics.get("memory_usage", 0))
