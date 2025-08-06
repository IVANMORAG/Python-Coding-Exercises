"""
EJERCICIO 182:
Crea una función obtener_ultimos_n_elementos que retorne 
los ultimos n elementos usando slicing.

Descripción:
Slice con índice negativo en listas.
"""

def obtener_ultimos_n_elementos(lista, n):
    
    return lista[-n:]

print(obtener_ultimos_n_elementos([1,2,3,4,5,6,7,8,9],2))