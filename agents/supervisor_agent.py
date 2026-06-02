class SupervisorAgent:
    def validate(self, diagnostics, plan, knowledge):
        explanation = f"""
        Issue detected: {diagnostics['issue']}
        Root cause inferred: {diagnostics['root_cause']}

        This recommendation is generated using:
        - Vision-based detection
        - Telemetry analysis
        - Retrieved SOP documents

        Knowledge Query: {knowledge['query']}
        """

        confidence = "HIGH" if diagnostics["risk_level"] == "HIGH" else "MEDIUM"

        return {
            "final_steps": plan["steps"],
            "explanation": explanation.strip(),
            "confidence_level": confidence
        }