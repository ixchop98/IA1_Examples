import cv2
import mediapipe as mp
#pip install mediapipe==0.10.9

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    total_fingers = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Puntos clave de los dedos
            landmarks = hand_landmarks.landmark

            tips_ids = [4, 8, 12, 16, 20]

            fingers = []

            # Pulgar (caso especial)
            if landmarks[tips_ids[0]].x < landmarks[tips_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Otros dedos
            for i in range(1, 5):
                if landmarks[tips_ids[i]].y < landmarks[tips_ids[i] - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total_fingers = sum(fingers)

    cv2.putText(frame, f'Dedos: {total_fingers}', (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("MediaPipe - Dedos", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
