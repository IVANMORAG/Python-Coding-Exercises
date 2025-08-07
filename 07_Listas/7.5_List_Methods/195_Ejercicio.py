"""
EJERCICIO 195:
Crea una función extender_lista que use extend() para agregar todos los 
elemetos de una lista a otra.

Descripción:
Método extend() para agregar múltiples elementos.
"""

def extender_lista(listaUno, listaDos):
    
    listaUno.extend(listaDos)
    
listaUno = [1,2,3]
listaDos = [9,8,7]

extender_lista(listaUno, listaDos)
print(listaUno)
    