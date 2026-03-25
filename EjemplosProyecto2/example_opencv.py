import cv2

# Inicializar detector de personas
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Abrir cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Redimensionar para mejorar rendimiento
    frame = cv2.resize(frame, (640, 480))

    # Detectar personas
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))

    # Dibujar resultados
    for (x, y, w, h) in boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar imagen
    cv2.imshow("Detección de Personas", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
