"""
EJERCICIO 72:
Crea una función duplicar_si_es_par que reciba un número 
y retorne el doble solo si es par, sino retorna el mismo 
número.

Descripción:
Sentencia if que modifica el valor de retorno.
"""

def duplicar_si_es_par(numero):
    if numero % 2 == 0:
        return numero * 2
    return numero
    
print(duplicar_si_es_par(6))