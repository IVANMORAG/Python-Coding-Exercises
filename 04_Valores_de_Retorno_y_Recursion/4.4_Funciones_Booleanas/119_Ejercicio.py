"""
EJERCICIO 119:
Escribe una función booleana todos_positivos que retorne 
True si todos los números en una lista son positivos.

Descripción:
Función booleana que verifica condición en toda la lista:
"""

def todos_positivos(lista):
    for numero in lista:
        if numero <= 0:
            return False
    return True

print(todos_positivos([1,5,6,-7,3]))