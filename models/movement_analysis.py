# models/movement_analysis.py

import numpy as np
from keras.models import load_model
from config.model_config import MOVEMENT_CONFIG

class MovementAnalyzer:
    def __init__(self):
        try:
            self.model = load_model(MOVEMENT_CONFIG['lstm_model_path'])
        except Exception as e:
            print("Could not load LSTM model. Using dummy movement analyzer.")
            self.model = None
        self.sequence_length = MOVEMENT_CONFIG['sequence_length']
        self.movement_threshold = MOVEMENT_CONFIG['movement_threshold']

    def analyze_movement(self, sequence):
        """
        Analyze a sequence of movement features.
        Return True if truancy (abnormal movement) is detected.
        """
        if self.model:
            sequence = np.array(sequence)
            sequence = sequence.reshape(1, self.sequence_length, -1)
            prob = self.model.predict(sequence)
            return prob[0][0] > self.movement_threshold
        else:
            # Dummy implementation: use average value as indicator.
            avg_movement = np.mean(sequence)
            return avg_movement > self.movement_threshold
