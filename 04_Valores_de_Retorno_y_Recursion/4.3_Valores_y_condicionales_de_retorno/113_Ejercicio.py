"""
EJERCICIO 113:
Define una función calcular_nota_final que retorne la nota si
ambos exámenes son >=60, o retorne -1 si alguno es <60.

Descripción:
Retorno condiional con validación previa.
"""

def calcular_nota_final(examen1, examen2):
    nota_final = (examen1 + examen2) / 2
    
    if nota_final >= 60:
        return nota_final
    else:
        return -1
    
print(calcular_nota_final(80, 90))