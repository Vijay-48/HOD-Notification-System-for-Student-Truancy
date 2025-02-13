# models/face_detection.py

from ultralytics import YOLO
import cv2
import numpy as np
from config.model_config import YOLO_CONFIG

class FaceDetector:
    def __init__(self):
        # Load the YOLOv8 (or YOLO11n) model using Ultralytics
        self.model = YOLO(YOLO_CONFIG['model_path'])
        self.conf_threshold = YOLO_CONFIG['confidence_threshold']

    def detect_faces(self, image):
        """
        Detect faces in an image using the YOLOv8 model.
        Returns a list of cropped face images.
        """
        results = self.model(image)  # Run inference on the image

        faces = []
        # The results can contain multiple predictions.
        for result in results:
            # result.boxes contains bounding boxes with .xyxy and .conf attributes.
            for box in result.boxes:
                conf = box.conf[0].item() if len(box.conf) > 0 else 1.0
                if conf < self.conf_threshold:
                    continue  # Skip detections with low confidence

                # Get bounding box coordinates (x1, y1, x2, y2)
                coords = box.xyxy[0].cpu().numpy().astype(int)
                x1, y1, x2, y2 = coords

                # Crop face from the original image (ensure indices are within image dimensions)
                face = image[y1:y2, x1:x2]
                faces.append(face)
        return faces
