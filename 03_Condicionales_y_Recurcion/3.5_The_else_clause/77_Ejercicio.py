"""
EJERCICIO 77:
Crea una función ontener_mayor que reciba dos números
y retorne el mayor de los dos.

Descripción:
if-eslse para comparar y retornar valores.
"""

def obtener_mayor(a, b):
    if a > b:
        return f"{a} es mayor"
    else:
        return f"{b} es mayor"

print(obtener_mayor(2, 5))