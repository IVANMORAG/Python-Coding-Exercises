"""
EJERCICIO 101:
Escrib una función imprimir_tabla_multiplicar que reciba
un número e imprima su tabla del 1 al 5. NO debe retornar nada.

Descripción:
Funcion que solo realiza acciones, no retorna valores.
"""

def imprimir_tabla_multiplicar(numero):
    for i in range(1, 6):
        resultado = i * numero
        print(f"{i} * {numero} = {resultado}")

imprimir_tabla_multiplicar(5)