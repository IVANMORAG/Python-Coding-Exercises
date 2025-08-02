"""
EJERCICIO 133:
Define una función contar_numeros_pares que reciba una lista
de números y cuente cuantos pares hay.

Descripción:
Contador con condición matemática.
"""

def contar_numeros_pares(lista_numeros):
    
    contador = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            contador = contador + 1
    return contador 

print(contar_numeros_pares([2,6,8,10,3])) 