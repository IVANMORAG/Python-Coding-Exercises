"""
EJERCICIO 127:
Crea una función acumular_producto que reciba una lista 
de números y retorne el producto de todos ellos.

Descripción:
Acumulador multiplicativo.
"""

def acumular_producto(lista):
    producto = 1
    
    for numero in lista:
        producto = producto * numero
        print("El producto es: ", producto)
    return producto

acumular_producto([1,4,5,6])