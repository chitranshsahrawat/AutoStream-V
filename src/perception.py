import cv2
import numpy as np
from ultralytics import YOLO

class PerceptionEngine:
    def __init__(self, model_path='yolov8n.pt'):
        # Nano model for edge-computing performance
        self.model = YOLO(model_path)
        
        # Engineering Constants for Distance Estimation
        # focal_length = (pixel_width_at_1m * distance_1m) / real_width
        self.FOCAL_LENGTH = 800  
        self.REAL_CAR_WIDTH = 1.8 # Average car width in meters

    def process(self, frame, conf=0.45):
        results = self.model(frame, conf=conf, verbose=False)
        annotated_frame = frame.copy()
        telemetry = []

        # Draw a 'Safety Horizon' line on the road
        height, width, _ = frame.shape
        cv2.line(annotated_frame, (0, int(height*0.8)), (width, int(height*0.8)), (255, 255, 255), 1)

        for box in results[0].boxes:
            coords = box.xyxy[0].tolist()
            x1, y1, x2, y2 = map(int, coords)
            cls_id = int(box.cls[0])
            label = self.model.names[cls_id]

            # Filter for relevant road objects
            if label in ['car', 'truck', 'bus', 'motorcycle']:
                pixel_width = x2 - x1
                
                # Math: Distance Estimation (Similar to Arene's depth perception logic)
                distance = (self.REAL_CAR_WIDTH * self.FOCAL_LENGTH) / pixel_width if pixel_width > 0 else 0
                
                # Safety Logic: Color-coded alerts
                # Red if < 7 meters, Green if Safe
                color = (0, 0, 255) if distance < 7 else (0, 255, 0)
                
                # Draw 3D-style bounding box effect
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
                cv2.rectangle(annotated_frame, (x1, y1-25), (x2, y1), color, -1)
                cv2.putText(annotated_frame, f"{label.upper()} | {distance:.1f}m", (x1 + 5, y1 - 7), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                
                telemetry.append({"type": label, "dist": distance})

        return annotated_frame, telemetry