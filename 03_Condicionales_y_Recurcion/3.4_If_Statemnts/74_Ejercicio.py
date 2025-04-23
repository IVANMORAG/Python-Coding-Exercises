"""
EJERCICIO 74:
Escribe una función procesar_lista_sino_es_vacía, 
que reciba una lista e imprima su longuitud, solo si
no esta vacía.

Descripcion:
Sentencia if, verificando longitud de la lista.
"""

def procesar_lista_sino_es_vacia(lista):
    if lista != []:
        return len(lista)
    return "Lista Vacia"

print(procesar_lista_sino_es_vacia([1,2,3, 90]))