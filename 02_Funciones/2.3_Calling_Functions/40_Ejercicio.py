"""
EJERCICIO 40;
Usa la función area_cuadrado, para calcular el 
área de un cuadrado de lado 7, y luego usa 
es_mayor para ver si esa área es mayor que 40.

Descripción:
Combinar resultados de múltiples funciones.
"""

def area_cuadrado(lado):
    return lado * lado

def es_mayor(num1, num2):
    return num1 > num2

area = area_cuadrado(7)
es_mayor_40 = es_mayor(area, 40)

print(es_mayor_40)