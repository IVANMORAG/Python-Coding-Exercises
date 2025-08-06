"""
EJERCICIO 173:
Define una función elemento_en_posicion que reciba una lista y un índice
y retorne el elemento en esa posicón de forma segura.

Descripción:
Acceso seguro a índices en listas.
"""

def elemento_en_posicion(lista, posicion):
    
    if len(lista) > 0 and posicion < len(lista):
        return lista[posicion]
    else:
        return "Fuera de rango o lista vacía"
    
print(elemento_en_posicion([1,2,3,4,5,6,7], 5))