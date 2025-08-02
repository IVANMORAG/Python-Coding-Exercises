"""
EJERCICIO 131:
Escribe una función contar_palabras que reciba un string y cuente 
cuantas palabras contiene (separadas por espacios).

Descripción:
Contador que icrementa cuando encuentra separadores.
"""

def contar_palabras(texto):
    if texto == "":
        return 0
    
    contador = 1
    
    for letra in texto:
        if letra == " ":
            contador = contador + 1
    return contador

print(contar_palabras("Tacos al pastor"))
            