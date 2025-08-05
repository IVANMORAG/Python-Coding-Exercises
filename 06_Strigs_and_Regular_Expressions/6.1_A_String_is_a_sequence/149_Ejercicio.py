"""
EJERCICIO 149:
Escribe una función recorrer_con_indices que imprima cada caracter de un string 
junto con su posicion.

Descripción:
Combinar índices con elemenos en bucles.
"""

def recorrer_con_indices(texto):
    
    for caracter in range(len(texto)):
        print(f"{caracter} = {texto[caracter]}")
    
    
recorrer_con_indices("Messi is the GOAT")