"""
EJERCICIO 176:
Escribe una función modificar_primer_elemento que 
cambie el primer elemento de una lista por un nuevo valor.

Descripcón:
Modificación directa de elementos en listas mutables.
"""

def modificar_primer_elemento(lista, valor):
    
    if len(lista) > 0:
        lista[0] = valor
        return lista
    else:
        return None
    
print(modificar_primer_elemento([1,3,5,7,9], 100))