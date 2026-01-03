from pyDatalog import pyDatalog

# Inicializa términos lógicos
pyDatalog.create_terms(
    'estudiante, nota, libro, aprobado, libro_antiguo, X, Y, N, L, A'
)

# --- Hechos ---
+estudiante('ana')
+estudiante('carlos')

+nota('ana', 85)
+nota('carlos', 75)

+libro('1984', ('George', 'Orwell'), 1949)

# --- Reglas ---
aprobado(X) <= nota(X, N) & (N >= 80)

libro_antiguo(L) <= libro(L, Y, A) & (A < 1950)

# --- Consultas ---
print("Estudiantes:", estudiante(X))
print("Aprobados:", aprobado(X))
print("Libros antiguos:", libro_antiguo(L))
print("Notas mayores a 80:", nota(X, N) & (N > 80))
