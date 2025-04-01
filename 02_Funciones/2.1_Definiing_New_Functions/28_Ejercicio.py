"""
EJERCICIO 28:
Define una función es_par que reciba un número 
y retorne True si es par, False si es impar.

Descripión:
Función con lógica condicional y retorno booleano.

Un número par es aquel número entero que es divisible 
entre 2, es decir, que al dividirlo por 2, el resultado 
es otro número entero sin residuo.
"""

def es_par(numero):
    return numero % 2 == 0

es_par(11)