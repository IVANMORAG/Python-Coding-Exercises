"""
EJERCICIO 145:
Crea una función buscar_todas_ocurrencias que reciba un string y un carácter, y 
retorne una lista con todos los índices donde aparece.

Descripción:
Búsqueda que encuentra múltiples coincidencias.
"""

def buscar_todas_ocurrencias(texto, caracter):
    
    posiciones = []
    
    for i in range(len(texto)):
        
        if texto[i] == caracter:
            posiciones.append(i)
            
    return posiciones


print(buscar_todas_ocurrencias("Tacos al pastor", "o"))