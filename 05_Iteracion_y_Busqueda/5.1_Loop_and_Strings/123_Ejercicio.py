"""
EJERCICIO 123:
Define una función construir_string que reciba un string 
y retorne una nueva versión con cada caracter duplicado.

Descripción:
Bucle que construye nuevo string procesando el original.
"""

def construir_string(texto):
    nuevo_texto = ""
    for letra in texto:
        nuevo_texto = nuevo_texto + letra + letra
        print(nuevo_texto)

construir_string("Hola mundo")