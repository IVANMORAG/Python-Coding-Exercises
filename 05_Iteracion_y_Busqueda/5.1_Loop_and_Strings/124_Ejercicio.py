"""
EJERCICIO 124:
Escribe una función eliminar_espacios que reciba un string
y retorne una versión sin espacios.

Descripción:
Bucle que filtra caracteres especificos
"""

def eliminar_espacios(texto):
    resultado= ""
    
    for recorrido in texto:
        if recorrido != " ":
            resultado = resultado + recorrido
    return resultado


print(eliminar_espacios("Tacos al Pastor"))