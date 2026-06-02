from utils.llm_client import LLMClient

class DiagnosticsAgent:
    def __init__(self):
        self.llm = LLMClient()

    def analyze(self, vision_result, telemetry):
        prompt = f"""
        Equipment: {vision_result['equipment']}
        Issue detected: {vision_result['issue']}
        Telemetry:
        - Temperature: {telemetry['temperature']}
        - Vibration: {telemetry['vibration']}

        Identify:
        1. Most likely root cause
        2. Risk level (LOW, MEDIUM, HIGH)

        Answer in JSON format:
        {{
            "root_cause": "...",
            "risk_level": "..."
        }}
        """

        response = self.llm.generate(prompt)

        try:
            import json
            parsed = json.loads(response)
        except:
            parsed = {
                "root_cause": "Unable to parse",
                "risk_level": "MEDIUM"
            }

        return {
            "equipment": vision_result["equipment"],
            "issue": vision_result["issue"],
            "root_cause": parsed["root_cause"],
            "risk_level": parsed["risk_level"]
        }