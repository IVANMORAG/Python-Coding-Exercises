"""
EJERCICIO 192:
Crea una función insertar_en_posicion que use insert() para agregar 
un elemento en una posicion especifica.

Descripción:
Método insert() para inserción en posición.
"""

def insertar_en_posicion(lista, posicion, elemento):
    if posicion < len(lista):
        lista.insert(posicion,elemento)
    else:
        return None

lista = [1,2,3,4,5,6,7,8,9]
posicion = 5
elemento = 90

insertar_en_posicion(lista, posicion, elemento)
print(lista)
    
