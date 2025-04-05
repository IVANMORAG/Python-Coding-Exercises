"""
EJERCICIO 37:
Escribe código que use la función suma_dos 
para sumar 8 + 12 y despues use doble 
con ese resultado.

Descripción:
Usar el resultado de una función como 
argumento de otra.
"""

def suma_dos(a, b):
    return a + b

def doble(numero):
    return numero * 2

suma = suma_dos(8, 12)
resultado_final = doble(suma)

print(resultado_final)