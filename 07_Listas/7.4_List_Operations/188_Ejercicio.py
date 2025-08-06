"""
EJERCICIO 188:
Define una lista elemento_existe que use el operador in para verificar 
si un elemento está en una lista.

Descripción:
Operador in para búsqueda en listas.
"""

def elemento_existe(lista, elemento):
    
    return elemento in lista

lista = [1,2,3,4,5,6,7,8,9]
elemento = 10

resultado = elemento_existe(lista, elemento)

print(resultado)