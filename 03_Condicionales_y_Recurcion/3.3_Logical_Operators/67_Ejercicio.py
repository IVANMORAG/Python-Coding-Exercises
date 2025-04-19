"""
EJERCICIO 67:
Crea una función es_multiplo_de_3_o_5, que retorne True, si un 
número es multiplo de 3 o 5.

Descripción:
Usar el operador or para alternativas.
"""

def es_multiplo_de_3_o_5(numero):
    return numero % 3 == 0 or numero % 5 == 0

print(es_multiplo_de_3_o_5(67))

