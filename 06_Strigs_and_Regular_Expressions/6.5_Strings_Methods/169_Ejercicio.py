"""
EJERCICI 169:
Escribe una función reemplazar_espacios que use replace() para 
combinar todos los espacios por guiones.

Descripción:
Usar el método replace() básico.
"""

def reemplazar_espacios(texto):
    return texto.replace(" ", "-")

print(reemplazar_espacios("Tacos al pastor."))

