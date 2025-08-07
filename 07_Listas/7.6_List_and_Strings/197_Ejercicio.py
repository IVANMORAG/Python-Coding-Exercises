"""
EJERCICIO 197:
Crea una función dividir_palabras que use split() para convertir una frase
en lista de palabras.

Descripción:
Método split() para crear listas desde strings
"""

def dividir_palabras(frase):
    
    if frase != "":
        return frase.split()
    else:
        return False
    
frase = "Tacos al pastor"
print(dividir_palabras(frase))
