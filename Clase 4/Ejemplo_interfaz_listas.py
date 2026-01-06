from pyDatalog import pyDatalog

# Declaración de términos
# Añadimos 'Z' para la lógica de recursividad si fuera necesaria
pyDatalog.create_terms('atomos, lista, pertenece, X, Y, L, Z')

# Hechos iniciales
+atomos('perro')
+atomos('gato')
+atomos('raton')

+lista('materias', ['matematicas', 'fisica', 'logica'])
+lista('ingredientes', ['huevo', 'harina', 'leche'])

# Regla: X pertenece a la lista L si existe un hecho lista(L, Y) y X está en la lista Y
# Usamos una función lambda o una comparación directa para verificar pertenencia en la lista de Python
pertenece(X, L) <= lista(L, Y) & (X.in_(Y))

# Interfaz interactiva
while True:
    print("\nOpciones:")
    print("1 - Agregar átomo")
    print("2 - Agregar lista")
    print("3 - Consultar pertenece(X, Lista)")
    print("4 - Salir")
    
    opcion = input("Seleccione una opción: ").strip()
    
    if opcion == '1':
        nuevo_atomo = input("Ingrese el nombre del átomo: ").strip()
        +atomos(nuevo_atomo)
        print(f"Hecho agregado: atomos({nuevo_atomo})")
        
    elif opcion == '2':
        nombre_lista = input("Ingrese el nombre de la lista: ").strip()
        elementos = input("Ingrese los elementos separados por coma: ").strip().split(',')
        elementos = [e.strip() for e in elementos]
        +lista(nombre_lista, elementos)
        print(f"Hecho agregado: lista({nombre_lista}, {elementos})")
        
    elif opcion == '3':
        consulta_elem = input("Ingrese el elemento a consultar: ").strip()
        consulta_lista = input("Ingrese el nombre de la lista: ").strip()
        
        # Ejecutamos la consulta
        resultado = pertenece(consulta_elem, consulta_lista)
        
        # En pyDatalog, una consulta vacía devuelve una lista vacía [], 
        # si hay coincidencia devuelve una lista con tuplas.
        if resultado:
            print(f"¡Sí! {consulta_elem} pertenece a {consulta_lista}.")
        else:
            print(f"No, {consulta_elem} no se encuentra en {consulta_lista}.")
        
    elif opcion == '4':
        break
    else:
        print("Opción no válida, intente de nuevo.")