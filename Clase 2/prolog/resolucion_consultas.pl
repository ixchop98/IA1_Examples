female(mary).
parent(C,M,F) :- mother(C,M), father(C,F).
mother(john, ann).  
mother(mary, ann).

father(mary, fred).
father(john, fred).

/*
Consulta verdadera:
    female(mary), parent(mary,M,F), parent(john, M, F).
    
Consulta falsa (backtracking):
    ?- female(mary), parent(mary, M, F), parent(pedro, M, F).
*/