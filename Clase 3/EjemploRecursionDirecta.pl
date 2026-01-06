/*
Recursión Directa
Una función se llama a sí misma en su definición.
*/
factorial(0, 1). % Caso base: factorial de 0 es 1 
factorial(N, F) :- 
     N > 0, 
     N1 is N - 1, 
     factorial(N1, F1), % Llamada recursiva 
     F is N * F1. 

/*
Aquí, la llamada recursiva ocurre antes de la multiplicación. 
Esto requiere que el intérprete mantenga cada llamada en la pila, 
lo que puede provocar desbordamientos para valores grandes de N.

*/