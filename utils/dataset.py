# utils/dataset.py

import os
import json
import cv2

def load_student_images(image_dir):
    """Load student images from the given directory."""
    images = {}
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            student_id = os.path.splitext(filename)[0]
            img_path = os.path.join(image_dir, filename)
            img = cv2.imread(img_path)
            images[student_id] = img
    return images

def load_json(json_path):
    """Load JSON data from a file."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data
