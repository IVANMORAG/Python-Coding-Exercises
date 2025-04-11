"""
EJERCICIO 48:
Crea una función duplicar_parametro que reciba un número,
lo duplique (modificando el parámetro), y lo retorne. Luego, 
prueba con una variable externa.

Descripción:
Los parámetros son variables locales.
"""

def duplicar_parametro(numero):
    numero = numero * 2
    return numero

mi_numero = 5
resultado = duplicar_parametro(mi_numero)

print(resultado)