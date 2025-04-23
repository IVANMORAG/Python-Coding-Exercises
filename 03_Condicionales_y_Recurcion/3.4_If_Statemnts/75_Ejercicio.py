"""
EJERCICIO 75:
Crea una funcion bonus_si_alto_puntaje, que reciba un 
puntaje y sume 100 puntos extra si el puntaje es mayor a 500.

Descripción: 
Sentencia if que modifica una varible.
"""

def bnus_si_alto_puntaje(puntaje):
    if puntaje > 500:
        return puntaje + 100
    return puntaje

print(bnus_si_alto_puntaje(550))