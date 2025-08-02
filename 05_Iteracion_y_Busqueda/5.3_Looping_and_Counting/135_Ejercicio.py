"""
EJERCICIO 135:
Crea una función contar_repeticiones que reciba un string y un carácter y cuente 
cuántas veces aparece ese carácter.

Descripción:
Contador especifico para un elemento.
"""

def contar_repeticiones(texto, letra):
    
    if texto == "":
        return 0
    
    contador_letra = 0
    
    for caracter in texto:
        if caracter == letra:
            contador_letra = contador_letra + 1
        
    return contador_letra

print(contar_repeticiones("Tacos al Pastor", "o"))