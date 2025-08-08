"""
EJERCICIO 204:
Escribe una función cotar_pares_lista que cuente cuantos números pares
hay en una lista.

Descripción:
Bucle con contador condicional.
"""

def contar_pares_lista(lista):
    
    contador = 0
    
    if lista != []:
        
        for elemento in lista:
            
            if elemento % 2 == 0:
                
                contador = contador + 1
        
        return contador
    
    return False

lista = [1,2,3,4,5,6,7,8,9]
print(contar_pares_lista(lista))