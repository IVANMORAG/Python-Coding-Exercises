"""
EJERCICIO 54:
Crea una función factorial_simple que calcule 
el factorial de 3 usando multiplicaciones sucesivas

Descripción:
Función con multiples operaciones locales.
"""

def factorial_simple():
    resultado = 1
    resultado = resultado * 1
    resultado = resultado * 2
    resultado = resultado * 3
    
    return resultado

fact_3 = factorial_simple()
print(fact_3)