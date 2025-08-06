"""
EJERCICIO 181:
Escribe una función obtener_primeros_n_elementos que use slicing
para retornar los primeros n elementos de una lista.

Descripción:
Slice básico desde el inicio de lista.
"""

def obtener_primeros_n_elementos(lista, n):
    
    return lista[:3]


print(obtener_primeros_n_elementos([1,2,3,4,5,6,7,8,9], 7))