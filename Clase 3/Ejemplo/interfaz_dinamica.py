from pyDatalog import pyDatalog

# Declaración de términos lógicos
pyDatalog.create_terms('animal, depredador, come, X, Y, Z')

# Hechos iniciales
+animal('raton')
+animal('serpiente')
+animal('halcon')

+depredador('serpiente', 'raton')
+depredador('halcon', 'serpiente')

# Regla recursiva: come
come(X, Y) <= depredador(X, Y)
come(X, Y) <= depredador(X, Z) & come(Z, Y)

# Interfaz interactiva
while True:
    print("\nOpciones:")
    print("1 - Agregar hecho animal")
    print("2 - Agregar hecho depredador")
    print("3 - Consultar relación come(X, Y)")
    print("4 - Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        nuevo_animal = input("Ingrese el nombre del animal: ").strip()
        +animal(nuevo_animal)
        print(f"Hecho agregado: animal({nuevo_animal})")
        
    elif opcion == '2':
        depredador_X = input("Ingrese el depredador: ").strip()
        depredador_Y = input("Ingrese la presa: ").strip()
        +depredador(depredador_X, depredador_Y)
        print(f"Hecho agregado: depredador({depredador_X}, {depredador_Y})")
        
    elif opcion == '3':
        consulta_X = input("Ingrese el animal depredador: ").strip()
        consulta_Y = input("Ingrese el animal presa: ").strip()
        resultado = come(consulta_X, consulta_Y)
        print(f"{consulta_X} come {consulta_Y}? {bool(resultado)}")
        
    elif opcion == '4':
        break
        
    else:
        print("Opción no válida, intente de nuevo.")
