from utils.llm_client import LLMClient

class PlanningAgent:
    def __init__(self):
        self.llm = LLMClient()

    def generate_plan(self, diagnostics, knowledge_docs):
        context = "\n".join(knowledge_docs[:2])

        prompt = f"""
        Equipment: {diagnostics['equipment']}
        Issue: {diagnostics['issue']}
        Root Cause: {diagnostics['root_cause']}

        Reference SOP:
        {context}

        Generate a step-by-step repair plan (max 5 steps).
        Keep it practical and technician-friendly.
        Return as bullet points.
        """

        response, tokens = self.llm.generate(prompt)
        self.last_tokens = tokens

        steps = [line.strip("- ").strip() for line in response.split("\n") if line.strip()]

        return {
            "issue": diagnostics["issue"],
            "root_cause": diagnostics["root_cause"],
            "steps": steps[:5]
        }