"""
EJERCICIO 116:
Escribe una función booleana es-multiplo que retorne
True si el primer número es múltiplo del segundo.

Descripción:
Función que retorna solo True o False.
"""

def es_multiplo(num1, num2):
    if num2 % num2 == 0:
        return True
    return False

print(es_multiplo(2, 6))