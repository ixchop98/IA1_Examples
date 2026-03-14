analizar_lista(L) :-
    length(L, N),
    write('Longitud de la lista: '), write(N), nl,

    member(X, L),
    write('Un elemento de la lista: '), write(X), nl,

    append(L1, L2, L),
    write('Primera parte: '), write(L1), nl,
    write('Segunda parte: '), write(L2), nl,

    reverse(L, R),
    write('Lista invertida: '), write(R), nl.

    % analizar_lista([a, b, c]).