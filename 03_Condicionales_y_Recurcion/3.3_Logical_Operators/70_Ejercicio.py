"""
EJERCICIO 70:
Crea una función fin_de_semana que reciba un string 
con el día de la semana y retorne True si es "Sabado" 
o "Domingo.

Descripción:
Usar or para comparar con multiples valores.
"""

def fin_de_semana(dia):
    return dia == "Sabado" or dia == "Domingo"

print(fin_de_semana("Sabado"))