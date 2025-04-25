"""
EJERCICIO 81:
Escribe una función clasificar_edad que reciba una edad y
retorne "Niño(0-12)", "Adolecente(13-17) o "Adulto(10+)".

Descripción:
ef-elif-else con multiples rango.
"""

def clasificar_edad(edad):
    if edad > 0 and edad <= 12:
        return "Niño(0-12)"
    elif edad >= 13 and edad < 18:
        return "Adolecente(13-17)"
    else:
        return "Adulto(18+)"
    
print(clasificar_edad(22))
        