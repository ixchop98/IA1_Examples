/*
1. Corte Verde (Green Cut)
Se utiliza para mejorar la eficiencia del programa sin cambiar los resultados que Prolog devolvería. 
Si eliminas un corte verde, el programa seguirá dando las mismas respuestas, pero tardará más porque explorará caminos innecesarios.

Propósito: Evitar búsquedas en ramas que sabemos que van a fallar o que son redundantes.
*/
max(X, Y, X) :- X >= Y, !.
max(X, Y, Y) :- X < Y.

/*
Aquí, si X >= Y es cierto, el corte dice: "No pierdas tiempo intentando la segunda regla, porque sabemos que X < Y será falso".

?- max(10, 5, Mayor).
?- max(3, 8, Mayor).

Seguimiento paso a paso (trace)
    ?- trace.
    ?- max(10, 5, M).
    
    Verás cómo Prolog entra en 10 >= 5, luego encuentra el ! (el corte) y automáticamente descarta la segunda regla (max(X, Y, Y)), 
    terminando la búsqueda de inmediato.

    Escribe ?- notrace. para desactivarlo.
*/  