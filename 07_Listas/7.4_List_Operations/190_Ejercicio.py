"""
EJERCICIO 190:
Crea una función crear_lista_numeros que use operadores para crear
una lista de números de 1 hasta n.

Descripción:
Usar operaciones para construir listas.
"""

def crear_lista(n):
    lista = []
    
    for elemento in range(1, n+1):
        
        lista = lista + [elemento]
        
    return lista

print(crear_lista(9))