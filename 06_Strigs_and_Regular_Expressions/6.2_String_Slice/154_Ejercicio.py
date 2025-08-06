"""
EJERCICIO 154:
Escribe una función cada_segundo_caracter que retorne un string con
solo los caracteres en posiciones pares.

Descripción:
Slice con step(paso)
"""

def cada_segundo_caracter(texto):
    
    return texto[::2]

print(cada_segundo_caracter("Hello World!!!"))