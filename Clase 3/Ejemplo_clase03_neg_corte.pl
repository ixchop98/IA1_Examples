% =========================
% Hechos
% =========================
hombre(juan).
hombre(pedro).

mujer(maria).

% =========================
% Negación como falla
% (implementación interna)
% =========================
no(P) :- P, !, fail.
no(_).

% =========================
% Consultas de ejemplo
% =========================
% ?- no(hombre(juan)).    % false
% ?- no(hombre(maria)).   % true
% ?- no(mujer(maria)).    % false
% ?- no(mujer(juan)).     % true

/*
📌 Nota importante
    En Prolog real, NO debes redefinir \+.
    Esto es solo didáctico para entender cómo funciona internamente.
    En práctica, siempre usa:
        \+ P
    
🧾 Frase final para recordar
    Negar en Prolog = intentar probar y fallar
*/