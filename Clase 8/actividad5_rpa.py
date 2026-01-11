import pyautogui
import time
import os

# Espera inicial para preparar el entorno
time.sleep(2)

# Abrir Microsoft Word (en Windows)
os.system("start winword")
time.sleep(3)

# Escribir los datos personales
pyautogui.typewrite("Nombre: Nombre Estudiante\n", interval=0.05)
pyautogui.typewrite("Carnet: 2021-12345\n", interval=0.05)
pyautogui.typewrite("Automatización realizada con Python y PyAutoGUI.\n", interval=0.05)

# Esperar para la captura
time.sleep(2)

# Tomar captura de pantalla
screenshot = pyautogui.screenshot()
screenshot.save("captura_rpa_word.png")

print("Proceso completado con éxito. Captura guardada como 'captura_rpa_word.png'.")
