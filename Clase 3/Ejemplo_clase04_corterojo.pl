/*
2. Corte Rojo (Red Cut)
Este tipo de corte sí cambia el significado lógico del programa. 
Si eliminas un corte rojo, el programa podría devolver respuestas incorrectas o adicionales que no deberían estar ahí. Se usa a menudo para manejar el concepto de "si no, haz esto".

Propósito: Definir reglas de exclusión mutua donde la segunda opción depende de que la primera haya fallado.
*/
recompensa(Puntaje, premio) :- Puntaje > 90, !.
recompensa(_, consuelo).

/*
Sin el corte, alguien con 95 puntos recibiría tanto el premio como el consuelo. 
El corte rojo obliga a que solo se llegue a "consuelo" si el puntaje no es mayor a 90

?- recompensa(150,R)
?- recompensa(15,R).
*/