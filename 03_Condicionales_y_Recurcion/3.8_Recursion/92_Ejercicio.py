"""
EJERCICIO 92:
Crea una función recursiva suma_hasta_n que calcule la suma
de 1 hasta n.

Descripción:
Recursión con acumulación matematica.
"""

def suma_hasta_n(n):
    if n <= 0:
        return 0
    return n + suma_hasta_n(n - 1)
    
    
print(suma_hasta_n(3))