from ultralytics import YOLO

class YOLOModel:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)

    def predict(self, image_path):
        results = self.model(image_path)

        detections = []
        for r in results:
            for box in r.boxes:
                detections.append({
                    "class": self.model.names[int(box.cls)],
                    "confidence": float(box.conf)
                })

        return detections