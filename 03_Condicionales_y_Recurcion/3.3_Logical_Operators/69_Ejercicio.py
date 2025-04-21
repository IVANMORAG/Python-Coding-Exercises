"""
EJERCICIO 69:
Escribe una función edad_valida, que retorne True 
si una edad esta entre 0 y 120. usando operadores 
logicos.

Descripción:
Combinar multiles condicionales and.
"""

def edad_valida(edad):
    return edad >= 0 and edad <= 120

print(edad_valida(22))