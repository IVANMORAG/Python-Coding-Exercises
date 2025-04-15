"""
EJERCICIO 59:
Escribe una función ultimo_digito que reciba 
un número entero y retorne su ultimo digito.

Descripción:
El último digito es el resto de dividir entre 10.
"""

def ultimo_digito(a):
    return a % 10 

print(ultimo_digito(55))