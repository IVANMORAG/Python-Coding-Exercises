"""
EJERCICIO 126:
Escribe una función acumular_suma que reciba una lista de números
y muestre como se va acumulando la suma paso a paso.

Descripción:
Variable acumuladora que se actualiza en cada iteración.
"""

def acumular_suma(lista):
    suma_total = 0 
    for numero in lista:
        suma_total = suma_total + numero
        print("La suma total es: ", suma_total)
    return suma_total

acumular_suma([2,5,6,7])