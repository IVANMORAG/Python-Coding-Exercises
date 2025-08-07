"""
EJERCICIO 191:
Escribe una función agregar_elemento que use append() para agregar un 
elemento al final de una lista.

Descripción:
Método append() básico.
"""

def agregar_elemento(lista, elemento):
    lista.append(elemento)

lista = [1,2,3,4,5]
elemento = 100

agregar_elemento(lista, elemento)
print(lista)
    