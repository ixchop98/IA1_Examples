
lista_de_tres(L) :-
    length(L, 3).


%Generar Una lista de tamaño N
crear_lista(N, L) :-
    length(L, N).

% Comprobar si son de la misma longitud
misma_longitud(L1, L2) :-
    length(L1, N),
    length(L2, N).



% lista_de_tres([a, b, c]).
% lista_de_tres([a, b]).
% crear_lista(4, L).
% misma_longitud([1,2,3], [a,b,c]).

