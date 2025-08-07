"""
EJERCICIO 200:
Crea una función crear_asincrono que tome una lista de palabras y retorne un 
acronimo con las primeras letras.

Descripción:
Procesar lista para crear string.
"""

def crear_asincrono(palabras):
    
    acronimo = ""
    
    for palabra in palabras:
        
        if len(palabra) > 0:
            acronimo = acronimo + palabra[0].upper()
        
    return acronimo

palabras = "Hola Mundo"

print(crear_asincrono(palabras))