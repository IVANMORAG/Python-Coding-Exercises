"""
EJERCICIO 155:
Crea una función invertir string que retorne un string 
a reves usando slicing.

Descripción:
Slice con step negatvo.
"""

def invertir_string(texto):
    
    return texto[::-1]

print(invertir_string("Messi"))