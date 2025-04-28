"""
EJERCICIO 88:
Define una función descuento_especial que aplique descuentos:
si la compra es >200, verifica si es cliente VIP (20% de descuento)
o regular (10% de descuento).

Descripción:
Condicional anidado para aplicar diferentes descuentos.
"""

def descuento_especial(compra, es_vip):
    if compra > 200:
        if es_vip:
            return compra * 0.8
        else:
            return compra * 0.9
    else:
        return compra
    
print(descuento_especial(201, True))