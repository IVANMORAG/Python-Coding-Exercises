"""
EJERCICIO 45:
Crea una función contar_pares, que reciba 
una lista de números y retorne cuántos números
pares hay.

Descripción:
Bucle con contador condicional:
"""

def contar_pares(numeros):
    contador = 0
    
    for numero in numeros:
        if numero % 2 == 0:
            contador = contador + 1
    
    return contador

resultado = contar_pares([1, 2, 3 ,4])
print(resultado)