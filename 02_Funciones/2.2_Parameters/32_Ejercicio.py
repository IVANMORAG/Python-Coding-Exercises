"""
EJERCICIO 32:
Define una función presentarse() con 
parámetros por defecto:
nombre="Anonimo" y edad=0.

Descrición:
Función con parámetros opcionales y valores
por defecto.
"""

def presentarse(nombre="anonimo", edad=0):
    return f"Hola, mi nombre es {nombre} y mi edad es {edad}"

presentarse()
