"""
EJERCICIO 96:
Escribe una función pedir_nombre que solicite al usuario su 
nombre y retorne un saludo personalizado.

Descripción:
Usar input() básico para obtener texto.
"""

def pedir_nombre(nombre):
    nombre = input("Ingresa tu nombre: ")
    return f"Hola {nombre}, bievenido a Python"

print(pedir_nombre(""))