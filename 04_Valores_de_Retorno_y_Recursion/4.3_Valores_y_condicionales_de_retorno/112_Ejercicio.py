"""
EJERCICIO 112:
Crea una función validar_password que retorne "Fuerte"
si tiene >8 carácteres, "Media" si tiene 5-8, o "Debil"
si tiene <5.

Descripción:
Retornar strings según condicionales de longuitud.
"""

def validar_password(password):
    if len(password) > 8:
        return "Fuerte"
    elif len(password) >= 5 and len(password) < 8:
        return "Media"
    else:
        "Debil"
        
print(validar_password("Mowowowow6"))