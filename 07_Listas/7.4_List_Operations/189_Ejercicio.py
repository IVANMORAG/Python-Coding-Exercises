"""
EJERCICIO 189:
Escribe una función combinar_y_repetir que concatene dos listas
y luego repita el resultado.

Descripción:
Combinar operaciones de listas.
"""

def combinar_y_repetir(lista1, lista2, n):
    
    lista_nueva = lista1 + lista2
    
    return lista_nueva * n

lista1 = [1,2,3]
lista2 = [4,5,6]

n = 3

resultado = combinar_y_repetir(lista1, lista2, n)
print(resultado)