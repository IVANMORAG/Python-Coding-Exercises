"""
EJERCICIO 115:
Crea una función buscar_en_lista que retorne el 
índice de un elemento, o -1 si no se encuentra.

Descripción:
Retorno condicional en bucles de búsqueda.
"""

def buscar_en_lista(lista, indice):
    if indice < len(lista):
        return lista[indice]
    else:
        return -1

print(buscar_en_lista([1,5,7,8,4], 0))