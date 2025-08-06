"""
EJERCICIO 172:
Crea un función obtener_ultimo_elemento que retorne el ultimo 
elemento de una lista usando índice negativo.

Descripción:
índices negativos en listas.
"""

def obtener_ultimo_elemento(lista):
    
    if len(lista) > 0:
        return lista[-1]
    else:
        return None
    
print(obtener_ultimo_elemento([1,2,3]))