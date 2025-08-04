"""
EJERCICIO 141:
Escribe una función buscar_primera_ocurrencia que reciba un string y un carácter
y retorne el índice de la primera aparición (0-1, sino existe).

Descripción:
Búsqueda lineal básica en strings.
"""

def buscar_primera_ocurrencia(texto, caracter):
    
    for i in range(len(texto)):
        
        if texto[i] == caracter:
            return i
    
    return -1

print(buscar_primera_ocurrencia("Hola mundo", "o"))