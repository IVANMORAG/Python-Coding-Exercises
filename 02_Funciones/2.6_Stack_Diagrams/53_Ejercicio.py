"""
EJERCICIO 53:
Escribe una función sumar_tres_numeros que llame a sumas_dos,
dos veces para sumar tres números.

Descripción
Llamadas anidadas de funciones.
"""

def suma_dos(a, b):
    return a + b

def sumar_tres_numeros(a, b, c):
    suma_parcial = suma_dos(a, b)
    suma_total = suma_dos(suma_parcial, c)
    return suma_total

resultado = sumar_tres_numeros(2, 3, 4)
print(resultado)