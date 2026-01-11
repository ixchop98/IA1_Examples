import pyautogui
import time
import os

# Esperar 2 segundos antes de comenzar
time.sleep(2)

# Abrir el Bloc de notas (solo Windows)
os.system("start notepad++")
time.sleep(1.5)

# Escribir texto en el Bloc de notas
pyautogui.typewrite("Hola! Esto fue escrito automáticamente con PyAutoGUI.\n", interval=0.05)
pyautogui.typewrite("Todo controlado por Python.\n", interval=0.05)
pyautogui.typewrite("Simulando el comportamiento de RobotGo en Go.\n", interval=0.05)

# Simular salto de línea
pyautogui.press('enter')

# Escribir una lista de palabras (similar a listas de Prolog)
palabras = ["Curiosidad", "Innovación", "Exploración"]
for palabra in palabras:
    pyautogui.typewrite(f"- {palabra}\n", interval=0.1)

# Esperar antes de finalizar
time.sleep(2)

# Mostrar mensaje final
print("Automatización completada exitosamente.")
