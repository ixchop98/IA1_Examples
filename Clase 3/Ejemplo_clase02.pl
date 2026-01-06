%Hechos
estudiante(ana).
estudiante(luis).

aprobado(ana).
%Hasta ahora solo sabemos que ana aprobó pero no sabemos si luis también lo hizo

gana_beca(X) :- estudiante(X), aprobado(X).
%Un estudiante gana la beca si es estudiante y ha aprobado.  

pierde_beca(X) :- estudiante(X), \+aprobado(X).
%Un estudiante pierde la beca si es estudiante y no se puede probar que haya aprobado.  
