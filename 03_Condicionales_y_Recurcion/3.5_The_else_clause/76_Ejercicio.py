"""
EJERCICIO 76:
Escribe una función clasificar_signo que imprima "Positivo"
si un número es mayor que 0, sino imprima "NO positivo"

Decripción:
if-else básico con dos opciones.
"""

def clasificar_signo(numero):
    if numero > 0:
        return "Es positivo"
    else:
        return "No pisitivo"
    
print(clasificar_signo(8))