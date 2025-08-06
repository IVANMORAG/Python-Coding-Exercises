"""
EJERCICIO 160:
Crea una función acumular_transformaciones que vaya construyendo un string
agregando cada caracter en mayuscla si es letra, o sin cambios si no lo es.

Descripción:
Acumulación de transformaciones en nuevo string.
"""

def acumular_transformaciones(texto):
    
    resultado = ""
    
    for caracter in texto:
        
        if caracter >= "a" and caracter <= "z":
            resultado = resultado + caracter.upper()
        else:
            resultado = resultado + caracter
    
    return resultado

print(acumular_transformaciones("messi is the goat"))