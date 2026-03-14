concatenar(L1, L2, L3) :-
    append(L1, L2, L3).

% concatenar([1,2], [3,4], L).

% dividir una lista en dos partes
% append(X, Y, [a,b,c]).


% Verficiar prefijo de una lista
prefijo(P, L) :-
    append(P, _, L).
%prefijo([a,b], [a,b,c,d]).


% Inserter un elemento en cualquier posición
insertar(X, L, R) :-
    append(L1, L2, L),
    append(L1, [X|L2], R).
% insertar(z, [a,b], R).

