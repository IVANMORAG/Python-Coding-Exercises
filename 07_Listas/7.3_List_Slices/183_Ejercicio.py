"""
EJERCICIO 183:
Define una función ontener_elementos_pares que retorne solo los
elementos en posiciones pares de una lista.

Descripción:
Slice con step para saltar elementos.
"""

def obtener_elementos_pares(lista):
    
    return lista[::2]

print(obtener_elementos_pares([1,2,3,4,5,6,7,8,9]))