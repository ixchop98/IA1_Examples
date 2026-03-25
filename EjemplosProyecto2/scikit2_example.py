import cv2
import mediapipe as mp
import numpy as np
from sklearn.ensemble import RandomForestClassifier

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)

X = []
y = []

model = RandomForestClassifier()
trained = False

cap = cv2.VideoCapture(0)

def extract_features(landmarks):
    points = [(lm.x, lm.y) for lm in landmarks]
    base = points[0]  # muñeca

    features = []
    for p in points[1:]:
        dist = np.linalg.norm(np.array(p) - np.array(base))
        features.append(dist)

    return features

print("Presiona:")
print("  h → guardar 'hola'")
print("  a → guardar 'adios'")
print("  t → entrenar modelo")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    label = "Sin detectar"

    key = cv2.waitKey(1) & 0xFF

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            features = extract_features(hand_landmarks.landmark)

            # ===== Guardar datos =====
            if key == ord('h'):
                X.append(features)
                y.append(0)
                print(f"Guardado HOLA ({len(X)})")

            elif key == ord('a'):
                X.append(features)
                y.append(1)
                print(f"Guardado ADIOS ({len(X)})")

            # ===== Entrenar =====
            elif key == ord('t') and len(X) > 20:
                model.fit(X, y)
                trained = True
                print("Modelo entrenado")

            # ===== Predecir =====
            if trained:
                pred = model.predict([features])[0]

                if pred == 0:
                    label = "HOLA ✋"
                else:
                    label = "ADIOS ✊"

    cv2.putText(frame, label, (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Detector de Gestos", frame)

    if key == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
