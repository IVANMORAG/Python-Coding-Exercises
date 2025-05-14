"""
EJERCICIO 125:
Crea una función alternar_mayusculas que reciba un string
y retorne una versión donde los caracteres en posiciones pares 
esten en máyuscula.

Descripción:
Bucle con índice para procesar posiciones especificas.
"""

def alternar_mayusculas(texto):
    resultado = ""
    
    for i in range(len(texto)):
        if i % 2 == 0:
            resultado = resultado + texto[1].upper()
        else:
            resultado = resultado + texto[i]
    return resultado

print(alternar_mayusculas("Hola mundo"))