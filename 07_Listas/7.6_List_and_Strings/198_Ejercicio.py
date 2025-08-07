"""
EJERCICIO 198:
Define una función unir_palabras que use join() para convertir una lista 
de palabras en una frase.

Descripción:
Método join() para crear strings desde listas()
"""

def unir_palabras(lista):
    
    if lista != []:
        return ''.join(lista)
    else:
        return False

lista = ["Hola", "Messi", "Te amo"]
print(unir_palabras(lista))