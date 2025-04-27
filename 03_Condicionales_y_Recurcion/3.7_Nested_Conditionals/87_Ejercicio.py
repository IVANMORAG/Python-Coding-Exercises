"""
EJERCICIO 87:
Crea una función evaluar_número que clasifique un número,si es 
positivo verifica si es par o impar, si no es positivo, verifica si es
0 o negativo.

Descripción:
Condicionales anidados con diferentes clasificaciones.
"""

def evaluar_numero(numero):
    if numero > 0:
        if numero % 2 == 0:
            return "Es número par"
        else:
            return "Es número impar"
    elif numero < 0:
        return "El número es negativo"
    else:
        return "Es cero"
    
print(evaluar_numero(10))