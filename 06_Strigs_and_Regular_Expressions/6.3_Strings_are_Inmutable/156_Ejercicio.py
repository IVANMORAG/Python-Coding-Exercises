"""
EJERCICIO 156:
Escribe una función intentar_cambiar_carater que demueste
que no se puede modificar un string directamente, y en su lugar 
retorne una nueva versión modificada.

Descripción:
Crear un nuevo string en lugar de modificar el original.
"""

def intentar_cambiar_caracter(texto, posicion, nuevo_caracter):

    if posicion < 0 or posicion >= len(texto):
        return texto
    
    return texto[:posicion] + nuevo_caracter + texto[posicion+1:]


print(intentar_cambiar_caracter("Taca campechano", 4, "o"))