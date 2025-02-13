# models/face_recognition.py

import os
import cv2
import glob
import numpy as np
import face_recognition
from utils.dataset import load_json

class FaceRecognizer:
    def __init__(self):
        # Lists to store known face encodings and corresponding student IDs
        self.known_encodings = []
        self.student_ids = []
        # Dictionary to store student metadata loaded from JSON (key: student_id)
        self.student_details = {}
        self.load_student_database()

    def load_student_database(self):
        """Load student metadata and compute face encodings from stored images."""
        metadata_path = os.path.join("data", "students.json")
        if os.path.exists(metadata_path):
            self.student_details = load_json(metadata_path)
        else:
            print("Student metadata file not found.")
            self.student_details = {}

        # Load each student image from data/Images (assumes filename = student_id.ext)
        image_files = glob.glob(os.path.join("data", "Images", "*.*"))
        for image_path in image_files:
            student_id = os.path.splitext(os.path.basename(image_path))[0]
            image = cv2.imread(image_path)
            if image is None:
                continue
            # Convert image from BGR (OpenCV default) to RGB for face_recognition
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # Get face encodings (list of encodings for each face found)
            encodings = face_recognition.face_encodings(rgb_image)
            if encodings:
                self.known_encodings.append(encodings[0])
                self.student_ids.append(student_id)
                print(f"Loaded encoding for student {student_id}")
            else:
                print(f"No face found in image for student {student_id}")

    def recognize_face(self, face):
        """
        Given a face image, compute its encoding and compare with known encodings.
        Returns a tuple (student_id, similarity) if a match is found; otherwise (None, None).
        """
        # Convert the face image to RGB
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb_face)
        if not encodings:
            return None, None
        encoding = encodings[0]
        
        # Compute distances between the encoding and all known encodings
        distances = face_recognition.face_distance(self.known_encodings, encoding)
        if len(distances) == 0:
            return None, None
        
        # Find the best match (smallest distance)
        min_distance = min(distances)
        threshold = 0.6  # Adjust this threshold as necessary
        if min_distance < threshold:
            index = np.argmin(distances)
            # Convert distance to a similarity score (optional)
            similarity = 1 - min_distance  # Higher similarity means a closer match
            return self.student_ids[index], similarity
        return None, None
