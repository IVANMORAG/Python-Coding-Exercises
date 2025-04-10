"""
EJERCICIO 47:
Escribe una función calcular que use variables locales
a = 5 y b = 3, y retorne una suma.
Luego crea variables globales: a = 100 y b = 50 y llama a la
función.

Descripción:
Variables locales no afectan las globales. 
"""

a = 100
b = 50

def calcular():
    a = 5
    b = 3
    return a+b

print(f"Suma función 'calcular()': {calcular()}")
