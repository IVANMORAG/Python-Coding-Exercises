"""
EJERCICIO 180:
Crea una función actualiar_elemento_si_existe que modifique un 
elemento en una posición especifica solo si la posición es 
valida.

Descripción:
Modificación segura de listas.
"""

def actualizar_elemento_si_existe(lista, posicion, valor):
    
    if len(lista) > 0:
        
        if posicion < len(lista):
            lista[posicion] = valor
            return lista
        else:
            return None
    
print(actualizar_elemento_si_existe([1,2,3,4,5,6], 4, 99))