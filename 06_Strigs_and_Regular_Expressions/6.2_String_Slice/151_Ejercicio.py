"""
EJERCICIO 151:
Escribe una función obtener_primeros_n que reciba un string y un número 
n, y retorne los primeros n caracteres.

Descripción:
Slice básico desde el inicio.
"""

def obtener_primeros_n(texto, n):
    
    if texto == "":
        return False
    
    return texto[:n]

print(obtener_primeros_n("Messi es el GOAT", 3))