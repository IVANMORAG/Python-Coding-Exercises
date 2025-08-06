"""
EJERCICIO 186:
Escribe una función concatenar_listas que use el operador +
para unir dos listas.

Descripción:
Concatenación de listas con +
"""

def concatenar_listas(lista1, lista2):
    return lista1 + lista2

listaUno = [1,2,3]
listaDos = [4,5,6]

resultado = concatenar_listas(listaUno, listaDos)
print(resultado)