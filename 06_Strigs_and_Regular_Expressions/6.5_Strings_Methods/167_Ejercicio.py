"""
EJERCICIO 167:
Crea una función contar_palabras_con_split que use el m+etodo 
split() para contar palabras en un texto.

Descripción:
Usar split() para dividir y contar.
"""

def contar_palabras_con_spit(texto):
    
    if texto.strip() == "":
        return 0
    
    palabras = texto.split()
    
    return len(palabras)


print(contar_palabras_con_spit("Hola"))