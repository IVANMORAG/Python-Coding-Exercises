"""
EJERCICIO 66:
Escribe una función es_positivo_y_par que reciba 
un número y retorne True si es positivo y Par.

Descripción:
Usa el operador and para combinar condicionales.
"""

def es_positivo_y_par(numero):
    return numero > 0 and numero % 2 == 0

print(es_positivo_y_par(190))