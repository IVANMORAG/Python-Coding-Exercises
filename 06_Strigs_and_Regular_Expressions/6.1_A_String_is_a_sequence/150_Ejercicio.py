"""
EJERCICIO 150:
Crea una función son_caracteres_iguales que compare los caracteres 
en la misma posición de dos strings y retorne True si todos coinciden.

Descripción:
Compararar strings carácter por carácter.
"""

def son_caracteres_iguales(texto1, texto2):
    
    if len(texto1) != len(texto2):
        return False
    
    for i in range(len(texto1)):
        
        if texto1[i] != texto2[i]:
            return False
    
    return True

print(son_caracteres_iguales("Hola", "Hola"))