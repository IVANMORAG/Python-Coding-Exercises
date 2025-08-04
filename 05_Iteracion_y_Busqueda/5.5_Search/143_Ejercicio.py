"""
EJERCICIO 143:
Define una función buscar_palabra_en_texto que reciba un texto y una 
palabra, y retorne True si la palabra aparece completa en el texto.

Descipción:
Busqueda de subcadenas en stings.
"""

def buscar_palabra_en_texto(texto, palabra):
    longitud_palabra = len(palabra)
    longitud_texto = len(texto)
    
    for i in range(longitud_texto - longitud_palabra + 1):
        coincide = True
        for j in range(longitud_palabra):
            if texto[i + j] != palabra[j]:
                coincide = False
                break
        if coincide:
            return True
    return False


print(buscar_palabra_en_texto("Tacos al pastor", "pastor"))