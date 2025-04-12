"""
EJERCICIO 50: 
Crea dos funciones: funcion_a que defina x = 10 y llame a funcion_b
y funcion_b que defina x = 20 e imprma a x.

Descripción:
Cada función tiene su propio scope.
"""

def funcion_a():
    x = 10
    funcion_b()
    
def funcion_b():
    x = 20
    print(x)
    
funcion_b()