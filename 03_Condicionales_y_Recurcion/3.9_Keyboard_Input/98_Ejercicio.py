"""
EJERCICIO 98:
Define una función calculadora_simple que pida dos 
números y retorne su suma.

Descrición:
Multiples inputs mumericos.
"""

def calculdora_simple(num1, num2):
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    
    return f"{num1} + {num2} = {num1 + num2}"

print(calculdora_simple("", ""))