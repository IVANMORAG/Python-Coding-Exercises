"""
EJERCICIO 51:
Escribe una función operación que reciba dos números,
los sume y llame a otra función mostrar_resultado pasándole esa suma.

Descripción:
Dos funciones en el stack simultáneamente.
"""

def operacion(a, b):
    suma = a + b
    mostrar_resultado(suma)
    
def mostrar_resultado(resultado):
    print(resultado)
    
operacion(5, 6)