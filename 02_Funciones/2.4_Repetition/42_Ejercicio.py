"""
EJERCICIO 42:
Crea una función suma_hasta_n que reciba un 
número n y retorne la suma de todos los números
desde 1 hasta n.

Descripción:
Función con bucle y acumulador.
"""

def suma_hasta_n(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total

suma_hasta_n(4)