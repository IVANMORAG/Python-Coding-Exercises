"""
EJERCICIO 102:
Crea una función obtener_precio_final que reciba precio e impuesto,
y retorne el precio total. Usala en otra función que calcule el cambio.

Descripción:
Función que retorna valor para ser usado en calculos posteriores.
"""

def obtener_precio_final(precio, impuesto):
    return precio + (precio * impuesto)

def calcular_cambio(precio, impuesto, dinero_pagado):
    precio_total = obtener_precio_final(precio, impuesto)
    return dinero_pagado - precio_total

print(calcular_cambio(30, .9, 200))