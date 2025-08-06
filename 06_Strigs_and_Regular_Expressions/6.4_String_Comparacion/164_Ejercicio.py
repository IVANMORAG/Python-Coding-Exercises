"""
EJERCICIO 164:
Escribe una función comparar_longuitudes que retorne el string más largo 
o "Igual Longuitud" si tienen la misma cantidad de caracteres.

Descripción:
Comparación por longuitud en lugar de contenido.
"""

def comparar_longuitudes(texto1, texto2):
    if len(texto1) > len(texto2):
        return texto1
    elif len(texto2) > len(texto1):
        return texto2
    else:
        return "Son iguales"
    
print(comparar_longuitudes("Messi", "CR7"))