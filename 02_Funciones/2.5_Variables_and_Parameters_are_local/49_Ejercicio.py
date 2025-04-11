"""
EJERCICIO 49:
Escribe una función procesar_lista(), que reciba
una lista y agregue 99 al final.

Descripción: 
Modificación de objetos mutables.
"""

def procesar_lista(lista):
    lista.append(99)
    
mi_lista = [1, 2, 3]
procesar_lista(mi_lista)

print(mi_lista)