"""
EJERCICIO 142:
Crea una función buscar_en_lista_numeros que reciba una lista 
de númneros y un valor, y retorne el índice donde se encuentran.

Descripción:
Búsqueda lineal en listas númericas.
"""

def buscar_en_lista_numeros(lista, valor):
    
    if lista == []:
        return False
    
    for i in range(len(lista)):
        
        if lista[i] == valor:
            return i
    
    return False

print(buscar_en_lista_numeros([5,2,6,7,8,9],7))