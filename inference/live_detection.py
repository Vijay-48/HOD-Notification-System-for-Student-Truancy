# inference/live_detection.py

import cv2
import time
import numpy as np
from models.face_detection import FaceDetector
from models.face_recognition import FaceRecognizer
from models.movement_analysis import MovementAnalyzer
from utils.db_handler import DBHandler
from utils.notification import send_email_notification

def process_cctv_stream():
    """
    Process the CCTV stream, detect faces, recognize students, analyze movement,
    and send a notification to the HOD if truancy is detected.
    """
    cap = cv2.VideoCapture(0)  # Change source if needed (e.g., RTSP stream)
    face_detector = FaceDetector()
    face_recognizer = FaceRecognizer()
    movement_analyzer = MovementAnalyzer()
    db_handler = DBHandler()
    
    movement_sequence = []
    sequence_length = 10

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect faces in the frame
        faces = face_detector.detect_faces(frame)
        if faces:
            for face in faces:
                student_id, similarity = face_recognizer.recognize_face(face)
                if student_id:
                    print(f"Recognized student: {student_id} (similarity: {similarity:.2f})")
                    
                    # Simulate extraction of a movement feature (dummy feature)
                    dummy_movement_feature = np.random.rand()
                    movement_sequence.append(dummy_movement_feature)
                    
                    if len(movement_sequence) >= sequence_length:
                        truancy = movement_analyzer.analyze_movement(movement_sequence[-sequence_length:])
                        if truancy:
                            details = f"Truancy detected for student {student_id}."
                            print(details)
                            db_handler.log_truancy(student_id, details)
                            
                            # Retrieve full student details from metadata
                            student_details = face_recognizer.student_details.get(
                                student_id,
                                {'id': student_id, 'name': 'Unknown', 'email': 'unknown@example.com'}
                            )
                            send_email_notification(student_details, additional_info=details)
                else:
                    print("Face not recognized.")
        
        cv2.imshow("CCTV Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        time.sleep(0.1)  # Simulate processing delay

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_cctv_stream()
