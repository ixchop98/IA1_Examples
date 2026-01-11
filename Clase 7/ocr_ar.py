import cv2
import pytesseract
import numpy as np

#Isntalacion tesseract https://github.com/UB-Mannheim/tesseract/wiki
# Configurar ruta de Tesseract si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#INSTALAR ESPECÍFICAMENTE ESTAS VERSIONES DE numpy y pandas
#pip uninstall numpy pandas -y
#pip install numpy==1.26.4 pandas==2.1.4

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
    # Suavizado para reducir ruido
    suavizado = cv2.GaussianBlur(grises, (5,5), 0)
    _, umbral = cv2.threshold(suavizado, 150, 255, cv2.THRESH_BINARY)
    return umbral

def extraer_texto(imagen):
    texto = pytesseract.image_to_string(imagen, lang='eng')
    return texto.strip()

def superponer_texto(imagen, texto):
    imagen_ar = imagen.copy()
    y0, dy = 30, 30
    for i, linea in enumerate(texto.split('\n')):
        y = y0 + i*dy
        cv2.putText(imagen_ar, linea, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    return imagen_ar

while True:
    print("\nOpciones:")
    print("1 - Cargar y mostrar imagen")
    print("2 - Preprocesar y mostrar imagen")
    print("3 - Extraer y superponer texto")
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
        img_ar = superponer_texto(img, texto)
        print("Texto detectado:\n", texto)
        cv2.imshow("Imagen AR con texto", img_ar)

    else:
        print("Opción no válida.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

