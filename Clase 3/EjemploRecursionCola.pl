/*
Recursión de Cola
*/
factorial_tail(N, F) :- factorial_helper(N, 1, F). 
factorial_helper(0, Acc, Acc). % Caso base 
factorial_helper(N, Acc, F) :- 
    N > 0, 
    N1 is N - 1, 
    Acc1 is Acc * N, 
    factorial_helper(N1, Acc1, F). 

/*
Acc actúa como un acumulador para llevar el resultado parcial.
?factorial_tail(5, R).   
*/
