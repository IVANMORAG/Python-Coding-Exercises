"""
EJERCICIO 128:
Define una función construir_prgresivamente que reciba un string 
y retorne una lista con todas las subcadenas progresivas.

Descripción:
Variable string que se va construyendo
"""

def construir_progresivamente(texto):
    resultado = []
    subcadena = ""
    
    for letra in texto:
        subcadena = subcadena + letra
        resultado.append(subcadena)
    return resultado
            
print(construir_progresivamente("Ola mundo"))