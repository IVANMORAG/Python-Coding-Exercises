"""
EJERCICIO 152:
Crea una función ontener_ultimos_n caracteres de
un string.

Descripción:
Slice con índice negativo.
"""

def obtener_ultimos_n(texto, n):
    
    return texto[-n:]

print(obtener_ultimos_n("Messi es el GOAT", 6))