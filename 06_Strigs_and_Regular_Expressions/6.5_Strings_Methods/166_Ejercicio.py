"""
EJERCICIO 166:
Escribe una función limpiar_texto que reciba un string y retorne 
una versión sin espacios al inicio y al final, y en minusculas.

Descripción:
Usar los métodos strip() y lower()
"""

def limpiar_texto (texto):
    return texto.strip().lower()

print(limpiar_texto("  Messi, te fuiste un 5 de agosto, vuelveee :c "))