"""
EJERCICIO 179:
Escribe una función reemplazar_negativos que cambie todos los números 
negativos de un lista por 0.

Descripción:
Modificación condicional de elementos.
"""

def reemplazar_negativos(lista):
    
    if len(lista) > 0:
        
        for i in range(len(lista)):
            
            if lista[i] < 0:
                
                lista[i] = 0
                
        return lista
    
    else:
        return None
    
print(reemplazar_negativos([-1, 2,3,4,6,-6]))