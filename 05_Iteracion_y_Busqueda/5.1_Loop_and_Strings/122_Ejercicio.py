"""
EJERCICIO 122:
Crea una función contar_vocales que reciba 
un string y retorne cuantas vocales contiene.

Descripción:
Bucle con contador para caracteres especifcos.
"""

def contar_vocales(texto):
    vocales = "aeiou"
    contador = 0
    
    for vocal in vocales:
        for letra in texto:
            if vocal == letra:
                contador = contador + 1
    return contador
    

print(contar_vocales("Hola mundo"))