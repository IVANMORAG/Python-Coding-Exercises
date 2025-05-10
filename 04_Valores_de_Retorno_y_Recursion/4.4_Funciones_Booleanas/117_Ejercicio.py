"""
EJERCICIO 17:
Crea una función booleana tiene_mayusculas que retorne True 
si un string contiene al menos una letra mayuscula.

Descripción.
Función booleana que examina strings.
"""

def tiene_mayusculas(texto):
    for caracter in texto:
        if caracter >= "A" and caracter <= "Z":
            return True
    return False

print(tiene_mayusculas("Hola Mundo"))