"""
EJERCICIO 207:
Crea una función obtener_lista_ordenada() que use sorted() para 
retornar una nueva lista ordenada sin modificar la original.

Descripción:
Función sorted() que retorna nueva lista.
"""

def obtener_lista_ordenada(lista):
    
    lista_nueva = sorted(lista)
    
    return lista_nueva

lista = [1,8,5,3,87,5]
print(obtener_lista_ordenada(lista))
print(f"Lista original: {lista}")