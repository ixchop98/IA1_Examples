from pyDatalog import pyDatalog

# 1. Inicializamos los términos y variables
# 'parent' es una función/regla, el resto son hechos y variables
pyDatalog.create_terms('female, mother, father, parent, C, M, F')

# 2. Definimos los Hechos (Facts)
+ female("mary")
+ mother("john", "ann")
+ mother("mary", "ann")
+ father("mary", "fred")
+ father("john", "fred")

# 3. Definimos la Regla (Rule)
# En Prolog: parent(C,M,F) :- mother(C,M), father(C,F).
parent(C, M, F) <= mother(C, M) & father(C, F)

# 4. Realizamos la Consulta (Query)
# En Prolog: ?- female("mary"), parent("mary", M, F), parent("john", M, F).
print("Buscando a M y F tales que mary sea hembra y compartan padres con john:")
resultado = female("mary") & parent("mary", M, F) & parent("john", M, F)

print(resultado)
print(resultado.data)