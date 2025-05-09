"""
EJERCICIO 114:
Escrbe una función dividir_seguro que retorne el resultado de a/b, o retorne 
0 si b es cero.

Descripción:
Retorno condicional para evitar errores
"""

def dividir_seguro(a, b):
    if b != 0:
        return a/b
    else:
        return 0
    
print(dividir_seguro(12, 0))