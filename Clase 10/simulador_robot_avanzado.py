# Simulación avanzada de robot en 2D y 3D
import pygame
from vpython import sphere, vector, rate, color
import threading
import math

# --- Funciones de simulación 2D ---
def simulacion_2d():
    pygame.init()
    ventana = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Simulación Robot 2D Avanzada")
    clock = pygame.time.Clock()

    # Estado inicial
    x, y, angulo = 300, 300, 0
    velocidad = 3
    tamaño_robot = (40, 20)
    running = True

    # Trayectoria predefinida (círculo)
    usar_trayectoria = False
    radio = 100
    centro_x, centro_y = 300, 300
    t = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    usar_trayectoria = not usar_trayectoria  # alternar trayectoria

        if usar_trayectoria:
            # Movimiento circular
            t += 0.03
            x = centro_x + radio * math.cos(t)
            y = centro_y + radio * math.sin(t)
            angulo = -math.degrees(t)
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                x += velocidad * pygame.math.Vector2(1, 0).rotate(-angulo).x
                y += velocidad * pygame.math.Vector2(1, 0).rotate(-angulo).y
            if keys[pygame.K_DOWN]:
                x -= velocidad * pygame.math.Vector2(1, 0).rotate(-angulo).x
                y -= velocidad * pygame.math.Vector2(1, 0).rotate(-angulo).y
            if keys[pygame.K_LEFT]:
                angulo += 3
            if keys[pygame.K_RIGHT]:
                angulo -= 3

        # Detección de bordes
        if x < 0: x = 0
        if x > 600: x = 600
        if y < 0: y = 0
        if y > 600: y = 600

        # Registro de posición y orientación
        print(f"2D - Posición: ({x:.1f}, {y:.1f}), Ángulo: {angulo:.1f}")

        # Dibujar robot
        ventana.fill((30, 30, 30))
        robot = pygame.Surface(tamaño_robot)
        robot.fill((0, 255, 0))
        rotado = pygame.transform.rotate(robot, angulo)
        rect = rotado.get_rect(center=(x, y))
        ventana.blit(rotado, rect.topleft)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# --- Simulación 3D ---
def simulacion_3d():
    robot3d = sphere(pos=vector(0, 0, 0), radius=0.5, color=color.green)
    angulo = 0
    radio = 2
    while True:
        rate(60)
        angulo += 0.03
        robot3d.pos = vector(radio * math.cos(angulo), 0, radio * math.sin(angulo))
        print(f"3D - Posición: ({robot3d.pos.x:.2f}, {robot3d.pos.y:.2f}, {robot3d.pos.z:.2f})")

# --- Ejecutar simulaciones en paralelo ---
#threading.Thread(target=simulacion_2d).start()
simulacion_3d()
