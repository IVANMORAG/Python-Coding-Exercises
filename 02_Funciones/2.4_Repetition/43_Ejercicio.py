"""
EJERCICIO 43:
Define una función imprimir_palabra_n_veces, que
reciba una palabra y un número, e imprima la palabra
ese número de veces.

Descripción:
Bucle que repíte una acción n veces.
"""

def imprimir_palabra_n_veces(palabra, numero):
    for i in range(numero):
        print(palabra)
    
        
resultado = imprimir_palabra_n_veces("Tacos", 5)
