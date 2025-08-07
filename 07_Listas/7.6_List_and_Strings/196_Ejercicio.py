"""
EJERCICIO 196:
Escribe una función string_a_lista_carateres que convierta un string 
en una lista de caracteres.

Descripción:
Convertir string a lista usando list()
"""

def string_a_lista_caracteres(texto):
    
    lista = []
    
    if texto != 0:
        
        lista = list(texto)
        
        return lista
    else:
        return False

texto = "Hola listas con strings"

print(string_a_lista_caracteres(texto))