import cv2

def cargar_imagen(ruta):
    imagen = cv2.imread(ruta)
    if imagen is None:
        print("No se pudo cargar la imagen. Verifique la ruta.")
        return None
    return imagen

def convertir_grises(imagen):
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

def detectar_bordes(imagen):
    return cv2.Canny(imagen, 100, 200)

def detectar_contornos(imagen):
    grises = convertir_grises(imagen)
    bordes = detectar_bordes(grises)
    contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    copia = imagen.copy()
    cv2.drawContours(copia, contornos, -1, (0,255,0), 2)
    return copia

while True:
    print("\nOpciones:")
    print("1 - Cargar y mostrar imagen")
    print("2 - Convertir a escala de grises")
    print("3 - Aplicar detección de bordes (Canny)")
    print("4 - Detectar y mostrar contornos")
    print("5 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '5':
        break

    ruta = input("Ingrese la ruta de la imagen: ").strip()
    img = cargar_imagen(ruta)
    if img is None:
        continue

    if opcion == '1':
        cv2.imshow("Imagen original", img)

    elif opcion == '2':
        gris = convertir_grises(img)
        cv2.imshow("Escala de grises", gris)

    elif opcion == '3':
        bordes = detectar_bordes(convertir_grises(img))
        cv2.imshow("Bordes detectados", bordes)

    elif opcion == '4':
        contornos = detectar_contornos(img)
        cv2.imshow("Contornos detectados", contornos)

    else:
        print("Opción no válida.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
