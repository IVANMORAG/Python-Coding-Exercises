"""
EJERCICIO 55:
Escribe una función convertir_y_operar que tome
dos números, los convierta a Strings, los concatene y luego convierta 
el resultado de vuelta a número.

Descripción:
Función con múltiples variables locales y transformaciones.
"""

def convertir_y_operar(a, b):
    num1 = str(a)
    num2 = str(b)
    
    conquetenar = num1 + num2
    numero_final = int(conquetenar)
    
    return numero_final

print(convertir_y_operar(2, 3))
    