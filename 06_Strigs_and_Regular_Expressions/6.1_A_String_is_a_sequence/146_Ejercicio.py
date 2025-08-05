"""
EJERCICIO 146:
Escribe una función obtener_primer_caracter que reciba un string
y retorne su primer caracter, o una cadena vacía si el string está vacio.

Descripción: 
Acceder a elementos de string por índice.
"""

def obtener_primer_caracter(texto):
    
    if len(texto) > 0:
        return texto[0]
    else:
        return ""
    

print(obtener_primer_caracter("Hola strings"))