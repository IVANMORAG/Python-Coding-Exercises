"""
EJERCICIO 177:
Crea una función itercambiar_elementos que intercambie los elementos
en dos posiciones de una lista.

Descripción:
Modificar múltiples posiciones de una lista.
"""

def intercambiar_elementos(lista, pos1, pos2):
    
    if pos1 < len(lista) and pos2 < len(lista):
        
        temp = lista[pos1]
        lista[pos1] = lista[pos2]
        lista[pos2] = temp
        
        return lista
    
print(intercambiar_elementos([1,2,3,4,5,6,7], 4, 6)) 