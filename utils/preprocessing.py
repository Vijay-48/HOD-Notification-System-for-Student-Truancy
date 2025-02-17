# utils/preprocessing.py

import cv2

def preprocess_image(image, target_size=(224, 224)):
    """Resize and normalize the image for model input."""
    image_resized = cv2.resize(image, target_size)
    image_normalized = image_resized / 255.0
    return image_normalized
