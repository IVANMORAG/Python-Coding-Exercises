"""
EJERCICIO 97:
Crea una función pedir_edad que solicite la edad al usuario y 
retorne el año en que nacío.

Descripción:
Convertir input a número y hacer cálculos.
"""

def pedir_edad(edad_str):
    edad_str = input("¿Cuál es tu edad? ")
    edad_int = int(edad_str)
    return f"Naciste en el año: {2025 - edad_int}"

print(pedir_edad(""))