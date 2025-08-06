"""
EJERCICIO 171:
Escribe una función obtener_primer_elemento, que reciba 
una lista y retorne su primer elemento o None si esta vacía.

Descripción:
Acceso por índice a listas como secuencias.
"""

def obtner_primer_elemento(lista):
    
    if lista == []:
        return None
    
    if len(lista) > 0:
        return lista[0]
    
print(obtner_primer_elemento([2,4,6]))