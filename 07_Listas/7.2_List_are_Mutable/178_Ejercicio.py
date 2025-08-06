"""
EJERCICIO 178:
Define una función duplicar_elementos que modifique una lista multiplicando 
cada elemento por 2.

Descripción:
Modificar todos los elementos de una lista.
"""

def duplicar_elementos(lista):
    
    if len(lista) > 0:
        
        for i in range(len(lista)):
            
            lista[i] = lista[i] * 2
        
        return lista
    
print(duplicar_elementos([2,4,6,8]))