#pip install mediapipe opencv-python tensorflow numpy

import cv2
import mediapipe as mp
import numpy as np
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

DATA_PATH = "data"
actions = ["hola", "adios", "gracias", "porfavor"]

no_sequences = 20      # cantidad de ejemplos
sequence_length = 30   # frames por gesto

# Crear carpetas
for action in actions:
    for seq in range(no_sequences):
        os.makedirs(os.path.join(DATA_PATH, action, str(seq)), exist_ok=True)

cap = cv2.VideoCapture(0)

def extract_keypoints(results):
    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]
        return np.array([[lm.x, lm.y, lm.z] for lm in hand.landmark]).flatten()
    else:
        return np.zeros(21*3)

for action in actions:
    for sequence in range(no_sequences):
        for frame_num in range(sequence_length):

            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            keypoints = extract_keypoints(results)

            npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
            np.save(npy_path, keypoints)

            cv2.putText(frame, f'{action} - seq {sequence}',
                        (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow('Recolectando', frame)

            if cv2.waitKey(10) & 0xFF == 27:
                break

cap.release()
cv2.destroyAllWindows()
