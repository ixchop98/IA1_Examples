hombre(juan).
hombre(pedro).


mujer(maria).


/*
% Consultas
?- \+ hombre(maria).
true.   % Porque no puede probar que maria sea hombre

?- \+ mujer(juan).
true.   % Porque no puede probar que juan sea mujer

?- \+ mujer(maria).
false.  % Porque puede probar que maria sí es mujer

*/