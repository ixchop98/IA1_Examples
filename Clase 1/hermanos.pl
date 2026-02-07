/* Hechos*/
padre(juan, maria).
padre(juan, jose).
padre(juan, carlos).
padre(juan, jorge).
padre(rodolfo, manuel).
padre(rodolfo, benito).


madre(ana, maria).
madre(ana, jose).
madre(lucia, carlos).
madre(lucia, jorge).
madre(ana, manuel).
madre(ana, benito).


/* Regla: dos personas son hermanos si comparten el mismo padre y no son la misma persona*/

hermano(X,Y) :- (padre(P,X) , padre(P,Y)  ) , (madre(M,X) , madre(M,Y) ) ,(X \= Y).  

mediohermano(X,Y) :- (padre(P,X) , padre(P,Y) ) , (madre(M,X) , madre(M2,Y) ,  (M \= M2)),(X \= Y) .
mediohermano(X,Y) :- (madre(M,X) , madre(M,Y) ) , (padre(P,X) , padre(P2,Y) ,  (P \= P2)),(X \= Y) .
/*


*/

/*Consulta*/

/*
hermano(maria,jorge)
mediohermano(maria,jorge)
hermano(maria,benito)
*/





/*
Pasos para ejecutar el archivo:
    swipl hermanos.pl
    Luego de ejecutar, prolog esperará a que ingresemos las consultas
    Por ejemplo: ?- hermano(maria,jorge).
    No olivdar colocar el punto al final
*/
