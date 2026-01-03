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
resultado = hermano(maria,jorge)
resultado2 = mediohermano(maria,jorge)
resultado3 = hermano(maria,benito)
*/

/*Resultado*/

/*
print(¿María y José son hermanos?,bool(resultado))
print(¿María y Jorge son medio hermanos?,bool(resultado2))
print(¿María y Jorge son medio hermanos?,bool(resultado3))
*/



