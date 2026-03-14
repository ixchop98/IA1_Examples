clasificacion(X, positivo) :- X > 0, !.
clasificacion(X, negativo) :- X < 0, !.
clasificacion(0, neutro).

