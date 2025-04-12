"""
EJERCICIO 52:
Crea una función calcular_cuadrado que reciba un número y 
retorne su cuadrado. Luego una función calcular_y_mostrar que 
llame a la primera e imprima el resultado.

Descripción:
Una función que llama a otra y usa su resultado.
"""

def calcular_cuadrado(numero):
    return numero ** 2

def calcular_y_mostrar(cuadrado):
    print(calcular_cuadrado(cuadrado))
    
calcular_y_mostrar(5)