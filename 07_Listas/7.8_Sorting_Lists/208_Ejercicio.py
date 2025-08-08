"""
EJERCICIO 208:
Define una función ordenar_descedente que ordene una lista de mayor 
a menor.

Descripción:
Parámetro reverse=True para orden descendente.
"""

def ordenar_descendente(lista):
    lista.sort(reverse=True)
    
lista = [23,45,7,3,5,32,2132]

ordenar_descendente(lista)
print(lista)