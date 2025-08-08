"""
EJERCICIO 202:
Crea una función sumar_todos que recorra ua lista de
números y retorne su suma total.

Descripción:
Bucle con acumulador en listas.
"""

def sumar_todos(lista):
    
    suma = 0
    
    if lista != []:
        
        for elemento in lista:
            
            suma = suma + elemento
            
        return suma
    
    else:
        return False

lista = [1,2,3,4,5]
print(sumar_todos(lista))