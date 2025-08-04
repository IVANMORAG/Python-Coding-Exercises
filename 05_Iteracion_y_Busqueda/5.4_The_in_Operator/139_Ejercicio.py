"""
EJERCICIO 139:
Escribe una función tiene_caracteres_especiales que retorne True
si un string contiene caracteres que no sean letras o números.

Descripción:
Combinar in con multiples conjuntos de caracteres.
"""

def tiene_caracteres_especiales(texto):
    
    if texto == "":
        return False
    
    caracteres_especiales = "-_,.@'*+<>!"
    
    for letra in texto:
        
        if letra in caracteres_especiales:
            return True
    
    return False

print(tiene_caracteres_especiales("Hola Mundo!"))