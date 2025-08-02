"""
EJERCICIO 132:
Crea una función contar Mayusculas que reciba un string y cuente
cuantas letras mayúsculas tiene.

Descipción:
Contador con condición especifica:
"""

def contar_mayusculas(texto):
    
    if texto == "":
        return 0
    
    contador = 0
    
    for letra in texto:
        if letra >='A' and letra <= 'Z':
            contador = contador + 1
    return contador

print(contar_mayusculas("Hola Mundo"))