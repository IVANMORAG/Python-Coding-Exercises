"""
EJERCICIO 44:
Escribe una función multiplicar_lista, que 
reciba una lista de números y un multiplicador y 
retorne una nueva lista con todos los números multiplicados.

Descripción:
Bucle que procesa cada elemento de una lista.
"""

def multiplicar_lista(numeros, multiplicador):
    resultado = []
    for numero in numeros:
        resultado.append(numero * multiplicador)
    return resultado

resultado = multiplicar_lista([1, 2, 3], 5)
print(resultado)