"""
EJERCICIO 203:
Define una función encontrar_maximo que recorra una lista y encuentre el valor 
máximo.

Descripción:
Bucle para encontrar extremos.
"""

def encontrar_maximo(lista):
    
    if lista != []:
        
        return max(lista)
    
    else:
        return False
    
lista = [1,80,3,4,5]

print(encontrar_maximo(lista))