"""
EJERCICIO 83:
Define una función precio_envio que retorne el costo 
del envió: gratis(>100), 10 pesos(50-100), 20 pesos(<50).

Descripcion:
Condicionales encadenados para diferentes costos.
"""

def precio_envio(precio):
    if precio > 100:
        return "El envió es gratis"
    elif precio > 50 and precio < 100:
        return "$10 del envió"
    else:
        return "$20 de envio"
    
print(precio_envio(250))