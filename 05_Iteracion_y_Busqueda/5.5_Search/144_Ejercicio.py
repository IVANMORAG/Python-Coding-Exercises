"""
EJERCICIO 144:
Escribe una función buscar_maximo_con_posicion que retorne tanto el 
valor maximo de una lista como una posicioń.

Descripción:
Búsqueda de elemento máximo manteniendo su índice.
"""

def buscar_maximo_con_posicion(numeros):
    if len(numeros) == 0:
        return None, -1
    
    maximo = numeros[0]
    posicion_maximo = 0
    
    for i in range(1, len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]
            posicion_maximo = i
    
    return maximo, posicion_maximo

print(buscar_maximo_con_posicion([1,2,3,6,4,3,90]))