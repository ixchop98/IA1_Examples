from pyDatalog import pyDatalog

# Declaración de términos lógicos
pyDatalog.create_terms('padre, madre, hermano, X, Y, P')

# Hechos
+padre('juan', 'maria')
+padre('juan', 'jose')
+madre('ana', 'maria')
+madre('ana', 'jose')

# Regla: dos personas son hermanos si comparten el mismo padre y no son la misma persona
hermano(X, Y) <= padre(P, X) & padre(P, Y) & (X != Y)

# Interfaz de consulta
while True:
    consulta = input("Ingrese una consulta (o 'salir' para terminar): ")
    if consulta.lower() == 'salir':
        break
    try:
        resultado = eval(consulta)
        print("Resultado:", bool(resultado))
    except Exception as e:
        print("Error en la consulta:", e)
