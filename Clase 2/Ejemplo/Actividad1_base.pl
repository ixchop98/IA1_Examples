% --- Hechos (Facts) ---
estudiante(ana).
estudiante(carlos).

nota(ana, 85).
nota(carlos, 75).

% En Prolog, 'autor' funciona como un "funtor" o estructura anidada
libro('1984', autor(george, orwell), 1949).

% --- Reglas (Rules) ---

% Un estudiante está aprobado si su nota N es mayor o igual a 80
aprobado(X) :- 
    nota(X, N), 
    N >= 80.

% Un libro es antiguo si su año de publicación A es menor a 1950
libro_antiguo(L) :- 
    libro(L, _, A), 
    A < 1950.

% --- Consultas Sugeridas (Queries) ---
% Para ejecutar estas consultas, escríbelas en la consola después de cargar el archivo:
%   Para ver el siguiente estudiante, debes presionar la tecla punto y coma
% ?- estudiante(X).
% ?- aprobado(X).
% ?- libro_antiguo(L).
% ?- nota(X, N), N > 80.