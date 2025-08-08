"""
EJERCICIO 206:
Escribe una función ordenar_lista que use sort() para ordenar una
lista de números de menor a mayor.

Descripción:
Método sort() básico que modifica la lista original.
"""

def ordenar_lista(lista):
    
    lista.sort()

lista = [2,5,7,8,4,5]

ordenar_lista(lista)
print(lista)