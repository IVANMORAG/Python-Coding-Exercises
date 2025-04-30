"""
EJERCICIO 91:
Escribe una función recusiva contar_regresivo que reciba 
un número n e imprima desde n hasa 1.

Descripción:
Recursión básica con caso base.
"""

def contar_regresivo(numero):
    if numero <= 0:
        return
    print(numero)
    contar_regresivo(numero-1)
    
contar_regresivo(10)