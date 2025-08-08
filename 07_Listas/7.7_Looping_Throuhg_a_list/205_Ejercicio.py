"""
EJERCICIO 205:
Crea una función crear_lista_cuadrados que recorra una lista de números 
y retorne una nueva lista con sus cuadrados.

Descripción:
Bucle para transformar elementos.
"""

def crear_lista_cuadrados(lista):
    
    lista_cuadrados = []
    
    if lista != []:
        
        for elemento in lista:
            
            lista_cuadrados.append(elemento * elemento)
            
        return lista_cuadrados
    else:
        return False
    
lista = [1,2,3,5]
print(crear_lista_cuadrados(lista))