"""
EJERCICIO 185:
Crea una función extraer_segmento que retorne una porción
de lista desde una posición inicial hasta una final.

Descripción:
Slice con inicio y fin especificos.
"""

def extraer_segmento(lista, inicio, fin):
    return lista[inicio:fin]

print(extraer_segmento([1,2,3,4,5,6,7,8,9], 2, 5))