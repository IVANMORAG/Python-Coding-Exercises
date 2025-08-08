"""
EJERCICIO 210:
Crea una función que retorne los3 números más grandes de una lista.

Descripción:
Combinar ordenamiento con slicig.
"""

def obtener_3(lista):
    
    lista.sort()
    
    return lista[-3:]

lista = [2,9,1,4,70]
print(obtener_3(lista))