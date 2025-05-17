"""
EJERCICIO 130:
Crea una función contar_consecutivos que reciba un strng 
y cuente la mayor cantidad de caracteres iguales consecutivos.

Descripción:
Variables que se actualizan para rastraer secuencias.
"""

def contar_consecutivos(texto):
    if len(texto) == 0:
        return 0
    
    max_consecutivos = 1
    consecutivos_actuales = 1
    
    for i in range(1, len(texto)):
        if texto[i] == texto[i-1]:
            consecutivos_actuales = consecutivos_actuales + 1
        else:
            if consecutivos_actuales > max_consecutivos:
                max_consecutivos = consecutivos_actuales
            consecutivos_actuales = 1
            
    if consecutivos_actuales > max_consecutivos:
        max_consecutivos = consecutivos_actuales
    
    return max_consecutivos


print(contar_consecutivos("Hello "))