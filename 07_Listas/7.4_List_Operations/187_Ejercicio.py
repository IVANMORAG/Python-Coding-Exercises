"""
EJERCICIO 187:
Crea una función repetir_lista que use el operador * para repetir una lista n veces.

Descripción:
Repetición de listas con +
"""

def repetir_lista(lista, n):
    return lista * n

lista = [1,2,3,5,6]
n = 5

resultado = repetir_lista(lista,n)

print(resultado)