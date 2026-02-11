# pip install pyswip
#⚠️ Importante:
#PySwip no incluye Prolog, solo lo conecta.
from pyswip import Prolog

prolog = Prolog()

#Cargar el archivo Prolog
prolog.consult("hermanos.pl")

#Hacer una consulta
resultado1 = list(prolog.query("hermano(maria, jose)"))
resultado2 = list(prolog.query("hermano(maria, carlos)"))

print(resultado1)
print(resultado2)