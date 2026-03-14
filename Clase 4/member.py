pertenece(X, L) :-
    member(X, L).

elemento_par(L, X) :-
    member(X, L),
    0 is X mod 2.


% pertenece(3, [1,2,3,4]).
% pertenece(5, [1,2,3,4]).

%Generar elementos de una lista
%member(X, [a, b, c]).

% Seleccionar los elementos que sean par 
% elemento_par([1,2,3,4], X).