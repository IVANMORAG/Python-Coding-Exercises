"""
EJERCICIO 84:
Escribe una función dia_tipo que reciba un numero 
(1-7) y retorne el día de la semana o invalido segun sea el caso.

Descripción:
elif multiple para mapear numeros a strings.
"""

def dia_tipo(dia_semana):
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    
    for dia in dias_semana:
        if dia_semana == dia:
            print(dia_semana)
        
dia_tipo("Lunes")