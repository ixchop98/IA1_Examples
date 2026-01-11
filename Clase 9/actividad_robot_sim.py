# Simulación 2D y 3D de un robot móvil
import pygame
import random
import time
from vpython import sphere, vector, color, rate, box

# --- Simulación 2D con Pygame ---
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación 2D del Robot")

# Posición inicial
x, y = width // 2, height // 2
path = [(x, y)]

# --- Simulación 3D con VPython ---
floor = box(pos=vector(0, 0, 0), size=vector(10, 0.1, 10), color=color.white)
robot3D = sphere(pos=vector(0, 0.5, 0), radius=0.3, color=color.red)

# --- Movimiento del robot ---
for step in range(20):
    dx, dy = random.choice([-10, 0, 10]), random.choice([-10, 0, 10])
    x += dx
    y += dy
    path.append((x, y))

    # Dibuja el entorno 2D
    screen.fill((30, 30, 30))
    for px, py in path:
        pygame.draw.circle(screen, (0, 255, 0), (px, py), 3)
    pygame.display.flip()

    # Actualiza entorno 3D
    robot3D.pos = vector(x/40 - 5, 0.5, y/40 - 5)
    rate(10)

    print(f"Paso {step+1}: X={x}, Y={y}")
    time.sleep(0.1)

pygame.quit()
print("Simulación completada.")
