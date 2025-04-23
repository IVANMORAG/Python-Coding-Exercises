"""
EJERCICIO 79:
Escribe una función precio_con_descuento,que aplique 10%
de descuento si el precio es mayor a 100, sino retorna 
el original.

Descripcion:
il-else con cálculos matemáticos.
"""

def precio_con_descuento(precio):
    if precio > 100:
        return precio * 0.9
    else:
        return precio
    
print(precio_con_descuento(101))
    