import streamlit as st

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