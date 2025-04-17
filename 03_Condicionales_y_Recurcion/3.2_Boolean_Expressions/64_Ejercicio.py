"""
EJERCICIO 64:
Escribe una función esta_en_rango que reciba un 
número y retorne True si esta entre 1 y 100.

Descripción:
Combinar dos comparaciones con >= y <=.
"""

def esta_en_rango(numero):
    return numero >= 1 and numero <= 100

print(esta_en_rango(101))