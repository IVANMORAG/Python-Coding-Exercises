"""
EJERCICIO 147:
Crea una función obtener_ultimo_digio que retorne el ultimo caracter de un string.

Descripción:
Usar índice negativo para acceder al final.
"""

def obtener_ultimo_digito(texto):
    
    if len(texto) > 0:
        return texto[-1]
    else:
        return " "
    

print(obtener_ultimo_digito("Amo a Messi"))