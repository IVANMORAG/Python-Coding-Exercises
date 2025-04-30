"""
EJERCICIO 90:
Crea una función calificacion_final que reciba examen y tareas. Si
ambos son >= 60, calcula promedio, sino,retorna "Reprobado".

Descripción: 
Verificar condicioes antes de hacer calculos.
"""

def calificacion_final(examen, tareas):
    if examen >= 60 and tareas >= 60:
        return (examen+tareas) / 2
    else:
        return "Reprobado"
    
print(calificacion_final(70, 90))