"""
EJERCICIO 161:
Escrib una función comparar_alfabeticamete que reciba dos strings
y retorne cual viene primero alfabeticamente.

Descripción:
Comparación lexicografica básica.
"""

def comparar_alfabeticamente(texto1, texto2):
    
    if texto1 < texto2:
        return texto1
    elif texto2 < texto1:
        return texto2
    else:
        return "SOn iguales"


print(comparar_alfabeticamente("arbol", "zorro"))