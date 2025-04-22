"""
EJERCICIO 73:
Define una función acceso_permitido que reciba
una edad e imprima "Acceso Permitido", si 
es mayor o igual a 18.

Descripción:
Sentencia if con condición de comparación.
"""

def acceso_permitido(edad):
    if edad >= 18:
        return "Acceso Permitido"
    return "Acceso Denegado"

print(acceso_permitido(22))