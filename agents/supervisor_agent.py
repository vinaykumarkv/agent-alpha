from utils.llm_client import LLMClient

class SupervisorAgent:
    def __init__(self):
        self.llm = LLMClient()

    def validate(self, diagnostics, plan, knowledge):
        prompt = f"""
        Issue: {diagnostics['issue']}
        Root Cause: {diagnostics['root_cause']}

        Steps:
        {plan['steps']}

        Knowledge Query: {knowledge['query']}

        Explain WHY these steps are correct in simple terms.
        Keep it concise and professional.
        """

        explanation, tokens = self.llm.generate(prompt)
        self.last_tokens = tokens

        confidence = "HIGH" if diagnostics["risk_level"] == "HIGH" else "MEDIUM"

        return {
            "final_steps": plan["steps"],
            "explanation": explanation,
            "confidence_level": confidence
        }