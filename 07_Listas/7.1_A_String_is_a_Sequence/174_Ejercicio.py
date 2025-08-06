"""
EJERCICIO 174:
Escribe una función recorrer_lista_con_indices que imprima cada 
elemeno de una lista junto con su índice.

Descripción:
Iterar sobre listas usando índices.
"""

def recorrer_lista_con_indices(lista):
    
    for i in range(len(lista)):
        print(f"{i} -> {lista[i-1]}")
    
recorrer_lista_con_indices([5,7,3,69])