from pyDatalog import pyDatalog

# Declaración de términos lógicos

pyDatalog.create_terms('padre, madre, hermano, mediohermano,  X, Y, P, M, M2, P2')

# Hechos
+padre('juan','maria')
+padre('juan','jose')
+madre('ana','maria')
+madre('ana','jose')

+padre('juan','carlos')
+padre('juan','jorge')
+madre('lucia','carlos')
+madre('lucia','jorge')

+madre('ana','manuel')
+madre('ana','benito')
+padre('rodolfo','manuel')
+padre('rodolfo','benito')


# Regla: dos personas son hermanos si comparten el mismo padre y no son la misma persona
hermano(X,Y) <= (padre(P,X) & padre(P,Y) & (X != Y) ) & (madre(M,X) & madre(M,Y) & (X != Y))
mediohermano(X,Y) <= (padre(P,X) & padre(P,Y) & (X != Y) ) & (madre(M,X) & madre(M2,Y) & (X != Y) & (M != M2))
mediohermano(X,Y) <= (madre(M,X) & madre(M,Y) & (X != Y) ) & (padre(P,X) & padre(P2,Y) & (X != Y) & (P != P2))

#Consulta
resultado = hermano('maria','jorge')
resultado2 = mediohermano('maria','jorge')
resultado3 = hermano('maria','benito')


#Resultado
print("¿María y José son hermanos?",bool(resultado))
print("¿María y Jorge son medio hermanos?",bool(resultado2))
print("¿María y Jorge son medio hermanos?",bool(resultado3))



