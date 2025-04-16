"""
EJERCICIO 58:
Define una función es_divisible que reciba dos múmeros 
y retorne True, si el primero es divisible por el segundo.

Descripción:
Un número es divisible por otro, si el resto es 0.
"""

def es_divisble(a, b):
    return a % b == 0

print(es_divisble(10, 6))