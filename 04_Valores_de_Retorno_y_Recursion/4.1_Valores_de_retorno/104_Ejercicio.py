"""
EJERCICIO 104:
Escribe una función convertir_minutos_a_horas que retorne las 
horas y minutos restantes. Usala en una función que calcule tiempo 
total de varias actividades.

Descripción:
Función que retorna múltiples valores.
"""

def convertir_minutos_a_horas(minutos_totales):
    horas = minutos_totales // 60
    minutos_restantes = minutos_totales % 60
    return horas, minutos_restantes

def tiempo_total_actividades(actividad1, actividad2, actividad3):
    total_minutos = actividad1 + actividad2 + actividad3
    horas, minutos = convertir_minutos_a_horas(total_minutos)
    return horas, minutos

print(tiempo_total_actividades(20, 30, 60))