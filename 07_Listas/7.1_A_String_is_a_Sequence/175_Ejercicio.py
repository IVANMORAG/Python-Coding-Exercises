"""
EJERCICIO 175:
Crea una función comparar_elementos que reciba dos listas y compare
elemento por elemento, retornando True si son iguales.

Descripción: 
Comparación elemento a elemento de secuencias.
"""

def comparar_elementos(lista1, lista2):
    
    for i in range(len(lista1)):
        
        if lista1[i] != lista2[i]:
            return False
    
    return True
        
print(comparar_elementos([2,1,3], [2,1,3]))