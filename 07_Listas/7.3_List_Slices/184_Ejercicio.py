"""
EJERCICIO 184:
Escribe una función invertir_lista_slice que retorne una lista
invertida usando slicing.

Descripción:
Slice con step negativo.
"""

def invertir_lista_slice(lista):
    
    return lista[::-1]

print(invertir_lista_slice([1,2,3,4,5,6,7,8,9]))