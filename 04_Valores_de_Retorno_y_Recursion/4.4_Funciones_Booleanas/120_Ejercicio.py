"""
EJERCICIO 20:
Crea una función booleana es-palindromo que verifique si un string 
se lee igual al derecho y al revés.

Descripión:
Función booleana con lógica de comparación compleja.
"""

def es_palindromo(texto):
    longuitud = len(texto)
    for i in range(longuitud // 2):
        if texto[i] != texto[longuitud-1-i]:
            return False
    return True

print(es_palindromo("olo"))