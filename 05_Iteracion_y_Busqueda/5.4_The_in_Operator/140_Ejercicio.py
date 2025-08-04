"""
EJERCICIO 140:
Crea una función elementos_comunes que reciba dos listas
y retorne una lista con los elementos que estan en ambas.

Descripción:
Usar in para encontrar intersección de listas.
"""

def elementos_comunes(lista1, lista2):
    
    if lista1 == [] or lista2 == []:
        return "No hay elementos en común"
    
    en_comun = []
    
    for elemento in lista1:
        
        if elemento in lista2:
            
            if elemento not in en_comun:
                en_comun.append(elemento)
                
    return en_comun
    
    
print(elementos_comunes([2,4,6,8], [2,3,6,9]))