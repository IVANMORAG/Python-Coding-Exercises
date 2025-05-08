"""
EJERCICIO 111:
Escribe una función obtener_descuento que retorne 0.1 
si el monto es >100, 0.005 si es >50, o 0 en otros casos.

Descripción:
Diferentes valores de retorno según condicionales.
"""

def obtener_descento(monto):
    if monto > 100:
        return 0.1
    elif monto > 50:
        return 0.005
    else:
        return 0

print(obtener_descento(200))