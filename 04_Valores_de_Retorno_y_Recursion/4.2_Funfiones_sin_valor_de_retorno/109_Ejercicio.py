"""
EJERCICIO 109:
Escribe una función dibujar_rectangulo que reciba ancho y alto
e imprima un rectangulo de asteriscos.

Descripción:
Función que genera un output visual sin retornar datos.
"""

def dibujar_rectangulo(ancho, alto):
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            linea = linea + "*"
        print(linea)
        
dibujar_rectangulo(10, 5)