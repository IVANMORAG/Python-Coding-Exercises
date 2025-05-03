"""
EJERCICIO 101:
Escribe una función calcular cuadrado que reciba un 
número y retorne su cuadrado. Luego otra función mostrar_cuadrado
que use la primera e imprima el resultado.

Descripción:
Distinguir entre funciones que retornan valores vs las que solo
imprimen.
"""

def calcular_cuadrado(numero):
    return numero ** 2

def mostrat_resultado(numero):
    resultado = calcular_cuadrado(numero)
    print("El cuadrado es: ", resultado)
    
mostrat_resultado(5)
    