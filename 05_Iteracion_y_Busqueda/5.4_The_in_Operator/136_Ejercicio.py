"""
EJERCICIO 136:
Escribe una función contiene_vocal que reciba un string y retorne 
True si contiene al menos una vocal.

Descripción:
Usar el operador in para verificar pertenencia.
"""
def contiene_vocal(texto):
    
    vocales = "aeiou"
    
    for letra in texto:
        if letra in vocales:
            return True 
    return False

print(contiene_vocal("Messi is the goat."))