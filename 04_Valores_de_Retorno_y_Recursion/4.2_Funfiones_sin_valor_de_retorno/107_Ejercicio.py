"""
EJERCICIO 107:
Crea una función saludar_multiple que reciba una lista de
nombres e impima un saludo para cada uno.

Descripción:
Función que procesa lista pero no retorna nada.
"""

def saludar_multipe(lista):
    for nombre in lista:
        print("Hola ", nombre)
        
        
saludar_multipe(["Ivan", "Luz", "Mora"])