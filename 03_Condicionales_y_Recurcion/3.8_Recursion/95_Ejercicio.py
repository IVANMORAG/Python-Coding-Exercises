"""
EJERCICIO 95:
Crea una función recursiva longuitud_string que calcule 
la longuitud de un string sin usar len().

Descripción: 
Recursión contando caracteres uno por uno.
"""

def longuitud_string(texto):
    if texto == "":
        return 0
    return 1 + longuitud_string(texto[1:])

print(longuitud_string("Tacos al pastor"))