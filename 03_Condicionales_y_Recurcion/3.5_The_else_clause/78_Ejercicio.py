"""
EJERCICIO 78:
Define una función clasifiacion_texto que reciba, una clasificación
númerica y retorne "Aprobado" si es mayor o igual a 60,
sino "reprobado".

Descripción:
if-else con diferentes tipos de retorno.
"""

def calificacion_texto(calificacion):
    if calificacion >= 60:
        return "Aprobado"
    else:
        return "Reprobado"
    
    
print(calificacion_texto(87))