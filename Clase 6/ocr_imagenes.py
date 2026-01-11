import cv2
import pytesseract

# Configurar ruta de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def cargar_imagen(ruta):
    imagen = cv2.imread(ruta)
    if imagen is None:
        print("No se pudo cargar la imagen. Verifique la ruta.")
        return None
    return imagen

def convertir_grises(imagen):
    return cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

def preprocesar_imagen(imagen):
    grises = convertir_grises(imagen)
    _, umbral = cv2.threshold(grises, 150, 255, cv2.THRESH_BINARY)
    return umbral

def extraer_texto(imagen):
    texto = pytesseract.image_to_string(imagen, lang='eng')
    return texto.strip()

while True:
    print("\nOpciones:")
    print("1 - Cargar y mostrar imagen")
    print("2 - Preprocesar y mostrar imagen")
    print("3 - Extraer texto de la imagen")
    print("4 - Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '4':
        break

    ruta = input("Ingrese la ruta de la imagen: ").strip()
    img = cargar_imagen(ruta)
    if img is None:
        continue

    if opcion == '1':
        cv2.imshow("Imagen original", img)

    elif opcion == '2':
        preproc = preprocesar_imagen(img)
        cv2.imshow("Imagen preprocesada", preproc)

    elif opcion == '3':
        preproc = preprocesar_imagen(img)
        texto = extraer_texto(preproc)
        print("Texto detectado:\n", texto)
        cv2.imshow("Imagen para OCR", preproc)

    else:
        print("Opción no válida.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
