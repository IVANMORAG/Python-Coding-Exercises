"""
EJERCICIO 118:
Define una función booleana es_triangulo_valido que verifique
si tres lados pueden formar un triángulo.

Descripción:
Funció booleana con validación matematica.
"""

def es_triangulo_valido(a,b,c):
    return a+b > c and a+c>b and b+c>a

print(es_triangulo_valido(2,9,1))