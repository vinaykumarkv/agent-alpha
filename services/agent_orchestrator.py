from utils.metrics import MetricsTracker

class AgentOrchestrator:
    def __init__(self, vision_agent, diagnostics_agent, retrieval_agent, planning_agent, supervisor_agent):
        self.vision_agent = vision_agent
        self.diagnostics_agent = diagnostics_agent
        self.retrieval_agent = retrieval_agent
        self.planning_agent = planning_agent
        self.supervisor_agent = supervisor_agent

    def execute(self, image_path):
        tracker = MetricsTracker()

        # Vision
        vision_result = self.vision_agent.analyze(image_path)

        telemetry = {
            "temperature": round(60 + 50 * vision_result["confidence"], 2),
            "vibration": round(0.5 + 1.0 * vision_result["confidence"], 2)
        }

        # Diagnostics
        diagnostics = self.diagnostics_agent.analyze(vision_result, telemetry)

        # Retrieval
        knowledge = self.retrieval_agent.fetch_knowledge(
            diagnostics["issue"],
            diagnostics["equipment"]
        )

        # Planning
        plan = self.planning_agent.generate_plan(
            diagnostics,
            knowledge["documents"]
        )

        # Supervisor
        final_output = self.supervisor_agent.validate(
            diagnostics,
            plan,
            knowledge
        )

        # ✅ Collect tokens
        total_tokens = (
            getattr(self.diagnostics_agent, "last_tokens", 0)
            + getattr(self.planning_agent, "last_tokens", 0)
            + getattr(self.supervisor_agent, "last_tokens", 0)
        )

        tracker.add_tokens(total_tokens)
        tracker.end()

        metrics = {
            "latency_sec": tracker.get_latency(),
            "tokens_used": total_tokens,
            **tracker.get_system_metrics()
        }

        return {
            "vision": vision_result,
            "telemetry": telemetry,
            "diagnostics": diagnostics,
            "knowledge": knowledge,
            "plan": plan,
            "final_output": final_output,
            "metrics": metrics
        }