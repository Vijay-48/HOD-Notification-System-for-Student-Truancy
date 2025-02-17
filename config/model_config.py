# config/model_config.py

# YOLO configuration parameters for face detection using YOLOv8
YOLO_CONFIG = {
    'confidence_threshold': 0.5,
    'model_path': 'models/yolov8n.pt',  # Path to your YOLOv8n (nano) weights file
    'class_names': ['face'],            # Adjust class names if needed
}

# Face Recognition configuration parameters
RECOGNITION_CONFIG = {
    'embedding_model_path': 'models/facenet_model.h5',  # Provide your FaceNet model
    'recognition_threshold': 0.6,
}

# Movement Analysis configuration parameters
MOVEMENT_CONFIG = {
    'lstm_model_path': 'models/movement_lstm.h5',  # Provide your trained LSTM model
    'sequence_length': 10,
    'movement_threshold': 0.5,
}

# Notification configuration parameters
NOTIFICATION_CONFIG = {
    'email': {
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587,
        'username': '21911a3548@vjit.ac.in',
        'password': 'hsxxhpoyzafiamnu',
        'from_email': '21911a3548@vjit.ac.in',
        'to_email': 'rockyvijju8@gmail.com'
    }
}
