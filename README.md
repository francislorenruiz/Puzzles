# Puzzles
Resuelve puzzles de cualquier tamaño donde cada pieza se representa con 4 números, uno para cada lado. El programa intentará encajar las piezas y encontrará una solución (si existe).

Dado un determinado tamaño de puzzle, se recogen los datos de las piezas de un fichero donde cada línea corresponderá a una pieza. Los 4 números deberán estar separados por un espacio y se cogerán de la siguiente forma:

    1º: Lado superior.
    2º: Lado derecho.
    3º: Lado inferior.
    4º: Lado izquierdo.
  
Por ejemplo, la siguiente pieza se representaría en el fichero:

        0
     _______
    |       |                       
  3 |       | 1                  -------> 0 1 2 3
    |_______|
        2
        
Cabe destacar que las piezas pueden rotarse, pero no darse la vuelta.

Se seguirán dos convenios para asegurar el correcto funcionamiento del programa:

  -Los bordes del puzzle se representarán siempre con el número cero.
  
  -Cada unión es única, por lo que no podrá haber dos uniones con el mismo número (números que siempre serán enteros positivos).
  
El puzzle ya montado se escribirá en otro fichero en el que las piezas seguirán el mismo formato que en el fichero de entrada (cada línea es una ficha y se compondrá de 4 números separados por espacios). La diferencia será que en este caso estarán rotadas y ordenadas por filas, de forma que la primera pieza será la de la esquina superior izquierda; la segunda será la que está a la derecha de la anterior; y así sucesivamente hasta acabar la fila, para posteriormente continuar con la primera de la siguiente fila.
Por ejemplo, para un puzzle 3x3 el resultado se guardaría en el fichero así:

     _______________________
    |       |       |       |                            (A) 0 1 2 0
    |   A   |   B   |   C   |                            (B) 0 3 4 1
    |_______|_______|_______|                            (C) 0 0 5 3
    |       |       |       |                            (D) 2 6 7 0
    |   D   |   E   |   F   |                --------->  (E) ...
    |_______|_______|_______|                            (F) ...
    |       |       |       |                            (G) ...
    |   G   |   H   |   I   |                            (H) ...
    |_______|_______|_______|                            (I) ...
