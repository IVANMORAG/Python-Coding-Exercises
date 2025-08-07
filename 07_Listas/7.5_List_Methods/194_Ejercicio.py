"""
EJERCICIO 194:
Escibe una funiń remover_por_posicion que use pop()
para eliminar y retornar un elemento en una posicion.

Descripción:
Método pop() para eliminación por índice.
"""

def remover_por_posicion(lista, posicion):
    
    if posicion > len(lista):
        return False
    else:
        return lista.pop(posicion)

lista = [1,2,3,4,5,6,7,8,9]
posicion = 5

print(remover_por_posicion(lista, posicion))
print(lista)