suma_lista([], 0). % Caso base: la suma de una lista vacía es 0 
suma_lista([X | XS], Suma) :- 
     suma_lista(XS, SumaResto), % Suma de la cola 
     Suma is X + SumaResto. % Suma total 
