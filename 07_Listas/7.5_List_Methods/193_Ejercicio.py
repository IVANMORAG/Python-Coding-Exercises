"""
EJERCICIO 193:
Define una función remover_elemento que use remove() para
eliminar la primera ocurrencia de un elemento.

Descripción:
Método remove() para eliminación por valor.
"""

def remover_elemento(lista, elemento):
    
    if elemento in lista:
        lista.remove(elemento)
    else:
        return None
    
lista = [1,2,3,4,5,6,7,8,9,0]
elemento = 0

remover_elemento(lista, elemento)
print(lista)