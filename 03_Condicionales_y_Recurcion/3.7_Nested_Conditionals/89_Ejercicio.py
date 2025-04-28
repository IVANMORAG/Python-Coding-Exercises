"""
EJERCICIO 89:
Escribe una función clasificar_triangulo que reciba 
tres lados y detrmine si es quilatero, isoceles o escaleno
(solo si forman un triangulo valido).

Descripción:
Primero verificar validez, luego clasificar.
"""

def clasificar_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            return "Equilatero"
        elif a == b or b == c or a == c:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "No es un traingulo valido"
    
print(clasificar_triangulo(4, 5, 7))