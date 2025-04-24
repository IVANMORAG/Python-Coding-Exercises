"""
EJERCICIO 82:
Crea una función nota_letra que convierta una calificacion numerica:
A (90-100), B(80-89), C(70-79), F(0-69).

Descripción:
Múltiples rangos númericos  con elif
"""

def nota_letra(calif):
    if calif >= 90 and calif <= 100:
        return "A"
    elif calif >= 80 and calif <= 89:
        return "B"
    elif calif >= 70 and calif <= 79:
        return "C"
    else:
        return "F"
    
print(nota_letra(87))