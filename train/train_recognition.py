# train/train_recognition.py

from models.face_recognition import FaceRecognizer
from utils.dataset import load_student_images

def train_face_recognition():
    """
    Dummy training for face recognition.
    Loads student images and computes/stores embeddings.
    """
    print("Training face recognition model...")
    images = load_student_images("data/Images")
    recognizer = FaceRecognizer()
    for student_id, image in images.items():
        embedding = recognizer.compute_embedding(image)
        recognizer.update_student_embedding(student_id, embedding)
        print(f"Processed embedding for student {student_id}")
    print("Face recognition model training complete.")
    
if __name__ == "__main__":
    train_face_recognition()
