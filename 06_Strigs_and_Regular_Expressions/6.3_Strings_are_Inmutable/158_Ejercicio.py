"""
EJERCICIO 158:
Define una función reemplazar primera vocal que retorne 
un nuevo string donde la primera vocal sea reemplazada por una X.

Descripción:
Construr un nuevo string modificando el original.
"""

def reemplazar_primera_vocal(texto):
    
    vocales = "aeiouAEIOU"
    
    for i in range(len(texto)):
        
        if texto[i] in vocales:
            return texto[:i] + "X" + texto[i+1:]
        
print(reemplazar_primera_vocal("SI podemos papu"))