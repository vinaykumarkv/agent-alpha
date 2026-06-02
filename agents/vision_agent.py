import random
from models.vision.yolov8_model import YOLOModel

class VisionAgent:
    def __init__(self, use_mock=True):
        self.use_mock = use_mock
        if not use_mock:
            self.model = YOLOModel()

    def analyze(self, image_path):
        if self.use_mock:
            return self._mock_analysis(image_path)
        else:
            return self._real_analysis(image_path)

    # ✅ Mock (FAST + controllable)
    def _mock_analysis(self, image_path):
        equipment_types = ["Hydraulic Pump", "Motor", "Control Panel"]
        issues = ["Overheating", "Leakage", "Loose Wiring"]

        result = {
            "equipment": random.choice(equipment_types),
            "issue": random.choice(issues),
            "confidence": round(random.uniform(0.75, 0.95), 2),
            "image_path": image_path
        }

        return result

    # ✅ Real YOLO detection (optional upgrade)
    def _real_analysis(self, image_path):
        detections = self.model.predict(image_path)

        if not detections:
            return {
                "equipment": "Unknown",
                "issue": "No issue detected",
                "confidence": 0.5,
                "image_path": image_path
            }

        # Simplified mapping logic
        detected_class = detections[0]["class"]

        return {
            "equipment": detected_class,
            "issue": "Possible anomaly",
            "confidence": detections[0]["confidence"],
            "image_path": image_path
        }
