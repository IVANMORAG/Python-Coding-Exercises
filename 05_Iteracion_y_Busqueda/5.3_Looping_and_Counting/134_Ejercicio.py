"""
EJERCICIO 134:
Escribe una función contar_par_rangos que reciba una lista de
edades y cuente cuantos están en cada rango: menores(0-17), adultos(18-64),
mayores(65+)

Descripción:
Múltiples contadores para diferentes caregorias.
"""

def contar_par_rangos(lista_edades):
    
    contador_menores = 0
    contador_adultos = 0
    contador_mayores = 0
    
    for edad in lista_edades:
        
        if edad > 0 and edad <= 17:
            contador_menores =contador_menores + 1
        elif edad >= 18 and edad <= 64:
            contador_adultos = contador_adultos + 1
        else:
            contador_mayores = contador_mayores + 1
    
    return f"Menores: {contador_menores}. \n Adultos: {contador_adultos}. \n Mayores: {contador_mayores}."

print(contar_par_rangos([2,45,90,80,22,12,45,67]))