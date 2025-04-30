"""
EJERCICIO 93:
Define ua función recsiva potencia que calcule base**exponente
sin usar **.

Descripción:
Recursión para calcular potencias.
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

print(potencia(2, 3))