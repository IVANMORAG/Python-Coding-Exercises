"""
EJERCICIO 94:
Escribe una función recursiva factorial que calcule n!.

Descripción:
El clásio ejemplo de recursión.
"""

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(3))