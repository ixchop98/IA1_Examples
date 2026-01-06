from pyDatalog import pyDatalog

pyDatalog.create_terms('X, Y, Z, N, S, R, M, maximo,elemento, suma_lista, suma_cola_logica, L, Acum, NuevoAcum')

# --- Hechos --- 
# (Los hechos 'elemento' no se usan en tus reglas actuales, pero están bien definidos)
+elemento(3)
+elemento(7)
+elemento(5)
+elemento(10)
+elemento(2)

# --- Máximo (Lógica pura sin funciones externas) ---
# Se define en dos reglas (como en Prolog)
maximo(X, Y, X) <= (X >= Y)
maximo(X, Y, Y) <= (X < Y)

# --- Suma Lista (Recursión Directa) ---
+suma_lista([], 0)
# Usamos una función lambda para separar cabeza y cola de forma segura
#suma_lista(L, S) <= (L != []) & (S == L[0] + R) & (suma_lista(L[1:], R))
suma_lista(L, S) <= (L != []) & (suma_lista(L[1:], R)) & (S == L[0] + R)

# --- Suma con Recursión de Cola (Estilo Lógico) ---
# Caso base: cuando la lista está vacía, el resultado es el acumulador
suma_cola_logica([], Acum, Acum)
# Caso recursivo: sumamos la cabeza al acumulador y seguimos
suma_cola_logica(L, Acum, R) <= (L != []) & (NuevoAcum == Acum + L[0]) & (suma_cola_logica(L[1:], NuevoAcum , R))

# --- Consultas ---
print("--- Resultados ---")
print(f"Máximo entre 7 y 10: {maximo(7, 10, N)}")
print(f"Suma [3,7,5] (Directa): {suma_lista([3,7,5], N)}")
# Para la cola, empezamos el acumulador en 0
print(f"Suma [3,7,5] (Cola): {suma_cola_logica([3,7,5], 0, N)}")

# Negación como falla (Python nativo)
no_pertenece = lambda E, L: E not in L
print(f"¿7 no está en [1,2,3]?: {no_pertenece(7, [1,2,3])}")