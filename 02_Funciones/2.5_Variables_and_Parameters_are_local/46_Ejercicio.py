"""
EJERCICIO 46:
Completa este código, ¿Qué valor tiene 
x después de llamar cambiar_valor()?

Descripción:
Variables locales vs globales.

Resultado: x vale 10(la x dentro de la función es local)
"""

x = 10

def cambiar_valor():
    x = 20
    
cambiar_valor()
print(x)