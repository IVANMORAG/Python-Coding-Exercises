"""
EJERCICIO 129:
Escribe una función actualizar que reciba una lista de números
y muestre cómo se va actualizando el valor maximo.

Descripción:
Variable que mantiene el máximo encontrado hasta el momento.
"""

def actualizar_maximo(numeros):
    if len(numeros) == 0:
        return None
    maximo = numeros[0]
    print("El inicial: ", maximo)
    
    for i in range(1, len(numeros)):
        if numeros[i] > maximo:
            maximo = numeros[i]
            print("Nuevo maximo: ", maximo)
    return maximo

print(actualizar_maximo([24,5,6]))