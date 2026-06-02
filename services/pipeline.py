from agents.vision_agent import VisionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.diagnostics_agent import DiagnosticsAgent
from agents.planning_agent import PlanningAgent
from agents.supervisor_agent import SupervisorAgent

from services.agent_orchestrator import AgentOrchestrator
from db.db_manager import log_event, log_recommendation

import json

# ✅ Initialize agents
vision_agent = VisionAgent(use_mock=False)
retrieval_agent = RetrievalAgent()
diagnostics_agent = DiagnosticsAgent()
planning_agent = PlanningAgent()
supervisor_agent = SupervisorAgent()

# ✅ Orchestrator
orchestrator = AgentOrchestrator(
    vision_agent,
    diagnostics_agent,
    retrieval_agent,
    planning_agent,
    supervisor_agent
)


def run_pipeline(image_path):

    # ✅ Run full orchestration
    results = orchestrator.execute(image_path)
    

    vision_result = results["vision"]
    telemetry = results["telemetry"]
    diagnostics = results["diagnostics"]
    knowledge = results["knowledge"]
    final_output = results["final_output"]
    metrics = results["metrics"]

    # ✅ Log event
    event_id = log_event(
        equipment_type=vision_result["equipment"],
        detected_issue=vision_result["issue"],
        confidence=vision_result["confidence"],
        image_path=image_path,
        telemetry=json.dumps(telemetry),
        metrics=json.dumps(metrics)
    )

    # ✅ Log recommendation
    log_recommendation(
        event_id,
        steps="\n".join(final_output["final_steps"]),
        risk=diagnostics["risk_level"],
        reasoning=final_output["explanation"],
        sources=knowledge["query"]
    )

    return {
        "event_id": event_id,
        **results
    }