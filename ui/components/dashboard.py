import streamlit as st

from db.db_manager import fetch_feedback

feedback_data = fetch_feedback()

def show_results(result):
    st.subheader("🔎 Detection")
    st.json(result["vision"])

    st.subheader("🧠 Diagnostics")
    st.json(result["diagnostics"])

    st.metric("⚠️ Risk Level", result["diagnostics"]["risk_level"])

    st.subheader("📚 Knowledge Retrieved")
    st.write(result["knowledge"]["documents"][0])

    st.subheader("🛠️ Recommended Steps")
    for step in result["final_output"]["final_steps"]:
        st.write(f"- {step}")

    st.subheader("📖 Explanation")
    st.write(result["final_output"]["explanation"])

    st.success(f"Confidence: {result['final_output']['confidence_level']}")

    
    if feedback_data:
        total = len(feedback_data)
        correct = sum(1 for f in feedback_data if f[0] == 1)

        accuracy = round((correct / total) * 100, 2)
        st.metric("✅ AI Accuracy (%)", accuracy)
        
    times = [f[0] for f in feedback_data if f[0] is not None]

    if times:
        avg_time = sum(times) / len(times)
        st.metric("⏱ Avg Resolution Time", round(avg_time, 2))


    


def show_metrics(metrics):
    import streamlit as st

    st.subheader("⚙️ System Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("⏱ Latency (sec)", metrics["latency_sec"])
    col2.metric("🧠 Tokens Used", metrics["tokens_used"])
    col3.metric("🖥 CPU Usage (%)", metrics["cpu_usage"])

    st.metric("💾 Memory Usage (%)", metrics["memory_usage"])