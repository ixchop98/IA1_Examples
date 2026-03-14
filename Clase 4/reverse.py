% verificar si una lista es palíndroma
palindroma(L) :-
    reverse(L, L).

% ?- palindroma([r,a,d,a,r]).

% ?- palindroma([a,b,c]).

%generar una lista original a partir de la invertida
% reverse(L, [a,b,c]).

%buscar el ultimo elemento de una lista
ultimo(L, X) :-
    reverse(L, [X|_]).

% ?- ultimo([1,2,3,4], X).

