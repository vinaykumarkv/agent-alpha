from agents.vision_agent import VisionAgent
from agents.retrieval_agent import RetrievalAgent
from db.db_manager import log_event, log_recommendation
import json

vision_agent = VisionAgent(use_mock=True) # Set to False to use real YOLO model (requires setup)
retrieval_agent = RetrievalAgent()


def run_pipeline(image_path):
    # STEP 1: Vision
    vision_result = vision_agent.analyze(image_path)

    # STEP 2: Telemetry simulation
    telemetry = {
        "temperature": round(60 + 50 * vision_result["confidence"], 2),
        "vibration": round(0.5 + 1.0 * vision_result["confidence"], 2)
    }

    # STEP 3: Log Event
    event_id = log_event(
        equipment_type=vision_result["equipment"],
        detected_issue=vision_result["issue"],
        confidence=vision_result["confidence"],
        image_path=image_path,
        telemetry=json.dumps(telemetry)
    )

    # STEP 4: Retrieve Knowledge
    knowledge = retrieval_agent.fetch_knowledge(
        vision_result["issue"],
        vision_result["equipment"]
    )

    # STEP 5: Create recommendation (simple for now)
    recommended_steps = "\n".join(knowledge["documents"])

    log_recommendation(
        event_id,
        steps=recommended_steps,
        risk="HIGH",
        reasoning="Based on retrieved SOP",
        sources="Manual Docs"
    )

    return {
        "event_id": event_id,
        "vision_result": vision_result,
        "telemetry": telemetry,
        "knowledge": knowledge,
        "recommended_steps": recommended_steps
    }