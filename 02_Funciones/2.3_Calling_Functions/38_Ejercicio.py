"""
EJERCICIO 38:
Crea una variable mi_nombre con tu nombre, luego
usa la función saludo_personalizado con esa
variable.

Descripción:
Usar variables como argumentos de funciones.
"""

mi_nombre = "Iván"

def saludo_personalizado(nombre):
    return "Hola " + nombre

saludo = saludo_personalizado(mi_nombre)
print(saludo)