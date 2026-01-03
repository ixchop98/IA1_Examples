
%editor pgm.prolog
    go :- reconsult('data.pl'),
        valsdedatos(A,B),
        SUMAEN is 0,
        for(A,B,SUMAEN,SUMASAL),nl,
        write('SUMA ='),write(SUMASAL),nl.
    /* El lazo for se ejecuta 'I'veces */
    for(I,B,SUMAEN,SUMASAL) :- not(I=0),
        B=[CABEZA|COLA],
        write(CABEZA),
        VALNUEVO is SUMAEN+CABEZA,
        for(I-1,ConsultasLA,VALNUEVO,SUMASAL).
    /* Si I es 0, devolver el valor calculado de SUMAEN */
    for(_,_,SUMAEN,SUMASAL) :- SUMASAL = SUMAEN.
    not(X) :- X, !, fail.
    not(_).



