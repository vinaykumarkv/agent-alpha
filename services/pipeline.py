from agents.vision_agent import VisionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.diagnostics_agent import DiagnosticsAgent
from agents.planning_agent import PlanningAgent
from agents.supervisor_agent import SupervisorAgent

from db.db_manager import log_event, log_recommendation

import json

vision_agent = VisionAgent(use_mock=True)
retrieval_agent = RetrievalAgent()
diagnostics_agent = DiagnosticsAgent()
planning_agent = PlanningAgent()
supervisor_agent = SupervisorAgent()


def run_pipeline(image_path):

    # ✅ Step 1: Vision
    vision_result = vision_agent.analyze(image_path)

    # ✅ Step 2: Telemetry simulation
    telemetry = {
        "temperature": round(60 + 50 * vision_result["confidence"], 2),
        "vibration": round(0.5 + 1.0 * vision_result["confidence"], 2)
    }

    # ✅ Step 3: Log event
    event_id = log_event(
        equipment_type=vision_result["equipment"],
        detected_issue=vision_result["issue"],
        confidence=vision_result["confidence"],
        image_path=image_path,
        telemetry=json.dumps(telemetry)
    )

    # ✅ Step 4: Diagnostics Agent
    diagnostics = diagnostics_agent.analyze(vision_result, telemetry)

    # ✅ Step 5: Retrieval Agent (RAG)
    knowledge = retrieval_agent.fetch_knowledge(
        diagnostics["issue"],
        diagnostics["equipment"]
    )

    # ✅ Step 6: Planning Agent
    plan = planning_agent.generate_plan(
        diagnostics,
        knowledge["documents"]
    )

    # ✅ Step 7: Supervisor Agent
    final_output = supervisor_agent.validate(
        diagnostics,
        plan,
        knowledge
    )

    # ✅ Step 8: Log recommendation
    log_recommendation(
        event_id,
        steps="\n".join(final_output["final_steps"]),
        risk=diagnostics["risk_level"],
        reasoning=final_output["explanation"],
        sources=knowledge["query"]
    )

    return {
        "event_id": event_id,
        "vision": vision_result,
        "diagnostics": diagnostics,
        "knowledge": knowledge,
        "plan": plan,
        "final_output": final_output
    }