"""
EJERCICIO 201:
Escribe una función imprir_elemenos que recorra una lista e
impima cada elemento.

Descripción:
Bucle básico sobre elemntos de lista.
"""

def imprimir_elementos(lista):
    
    if lista != []:
        
        for elemento in lista:
            print(elemento)
    else:
        return "No hay elementos"
    
lista = [1,2,3,4,5,6]
imprimir_elementos(lista)