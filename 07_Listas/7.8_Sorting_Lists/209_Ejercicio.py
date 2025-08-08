"""
EJERCICIO 209:
Escribe una función ordenar_palabras_alfabeticamente que ordene
una lista de strings algabeticamente.

Descripción:
Sort() funciona tambien con strings.
"""

def ordenar_palabras_alfabeticamente(lista):
    
    lista.sort()
    
lista = ["messi", "cr7", "gol"]
ordenar_palabras_alfabeticamente(lista)
print(lista)