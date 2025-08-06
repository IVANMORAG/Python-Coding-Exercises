"""
EJERCICIO 153:
Define una función obtener_medio que retorne la parte 
central de un string, excluyendo el primer y ultimo carácter.

Descripción:
Slice con inicio y fin especifico.
"""

def obtener_medio(texto):
    
    if len(texto) <= 2:
        return ""
    
    return texto[1:-1]

print(obtener_medio("Messi"))