class PlanningAgent:
    def generate_plan(self, diagnostics, knowledge_docs):
        issue = diagnostics["issue"]
        root_cause = diagnostics["root_cause"]

        steps = []

        # Extract steps from retrieved knowledge
        if knowledge_docs:
            raw_text = knowledge_docs[0]

            for line in raw_text.split("\n"):
                line = line.strip()
                if line.startswith("-"):
                    steps.append(line.replace("-", "").strip())

        # Add fallback steps if nothing found
        if not steps:
            steps = [
                "Inspect affected component",
                "Check system stability",
                "Restart equipment after inspection"
            ]

        return {
            "issue": issue,
            "root_cause": root_cause,
            "steps": steps[:5]  # limit steps
        }