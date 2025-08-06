"""
EJERCICIO 159:
Escribe una función construir_string_modificado qe tome un string 
y construya uno nuevo intercalando cada caracter con un guion.

Descrpción:
Construir completamente nuevo string.
"""

def construir_string_modificado(texto):
    
    if len(texto) == 0:
        return ""
    
    resultado = texto[0]
    
    for i in range(1, len(texto)):
        resultado = resultado + "-" + texto[i]
        
    return resultado

print(construir_string_modificado("Hola"))