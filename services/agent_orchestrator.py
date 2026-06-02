class AgentOrchestrator:
    def __init__(self, vision_agent, diagnostics_agent, retrieval_agent, planning_agent, supervisor_agent):
        self.vision_agent = vision_agent
        self.diagnostics_agent = diagnostics_agent
        self.retrieval_agent = retrieval_agent
        self.planning_agent = planning_agent
        self.supervisor_agent = supervisor_agent

    def execute(self, image_path):
        # ✅ Step 1: Vision
        vision_result = self.vision_agent.analyze(image_path)

        # ✅ Step 2: Telemetry simulation
        telemetry = {
            "temperature": round(60 + 50 * vision_result["confidence"], 2),
            "vibration": round(0.5 + 1.0 * vision_result["confidence"], 2)
        }

        # ✅ Step 3: Diagnostics
        diagnostics = self.diagnostics_agent.analyze(vision_result, telemetry)

        # ✅ Step 4: Retrieval (RAG)
        knowledge = self.retrieval_agent.fetch_knowledge(
            diagnostics["issue"],
            diagnostics["equipment"]
        )

        # ✅ Step 5: Planning
        plan = self.planning_agent.generate_plan(
            diagnostics,
            knowledge["documents"]
        )

        # ✅ Step 6: Supervisor validation
        final_output = self.supervisor_agent.validate(
            diagnostics,
            plan,
            knowledge
        )

        return {
            "vision": vision_result,
            "telemetry": telemetry,
            "diagnostics": diagnostics,
            "knowledge": knowledge,
            "plan": plan,
            "final_output": final_output
        }
