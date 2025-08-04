"""
EJERCICIO 137:
Crea una función es número_valido  que reciba un string y retorne
True si todos sus caracteres son dígitos.

Descripción:
Usar in para verificar carácteres validos.
"""

def numero_valido(texto):
    
    if texto == "":
        return False
    
    digitos = "0123456789"
    
    for caracter in texto:
        
        if caracter not in digitos:
            return False
        
    return True

print(numero_valido("23"))
    
    