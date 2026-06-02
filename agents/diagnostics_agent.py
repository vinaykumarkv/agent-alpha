class DiagnosticsAgent:
    def analyze(self, vision_result, telemetry):
        issue = vision_result["issue"]
        equipment = vision_result["equipment"]

        temperature = telemetry["temperature"]
        vibration = telemetry["vibration"]

        root_cause = ""
        risk_level = "MEDIUM"

        if issue == "Overheating":
            if temperature > 90:
                root_cause = "Possible coolant blockage or excessive load"
                risk_level = "HIGH"
            else:
                root_cause = "Minor heat fluctuation"

        elif issue == "Loose Wiring":
            if vibration > 1.0:
                root_cause = "Wiring loosened due to vibration"
                risk_level = "HIGH"
            else:
                root_cause = "Connection instability"

        elif issue == "Leakage":
            root_cause = "Seal or joint failure"
            risk_level = "HIGH"

        else:
            root_cause = "Unknown issue"

        return {
            "equipment": equipment,
            "issue": issue,
            "root_cause": root_cause,
            "risk_level": risk_level
        }