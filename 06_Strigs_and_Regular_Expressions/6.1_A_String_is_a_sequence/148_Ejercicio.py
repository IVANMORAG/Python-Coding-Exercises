"""
EJERCICIO 148:
Define una función caracter_en_posicion que reciba un string y un índice,
y retorne el carácter en esa posición( o fuera de rango, si el índice no existe)

Descripción:
Acceso seguro a índices de string.
"""

def caracter_en_posicion(texto, indice):
    
    if indice >= 0 and indice < len(texto):
        return texto[indice]
    else:
        return " "
    

print(caracter_en_posicion("Messi", 2))