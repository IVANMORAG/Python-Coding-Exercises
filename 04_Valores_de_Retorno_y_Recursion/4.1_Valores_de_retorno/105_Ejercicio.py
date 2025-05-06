"""
EJERCICIO 105:
Crea una función obtener_estadisticas que reciba una lista 
de numeros y retorne la suma, el promedio y la cantidad. Úsala 
para analizar datos.

Descripción:
Función que procesa datos y retorna múltiples resultados.
"""

def obtener_estadisticas(numeros):
    suma_total = 0
    
    for numero in numeros:
        suma_total = suma_total + numero
    
    cantidad = len(numeros)
    promedio = suma_total / cantidad
    
    return suma_total, promedio, cantidad


def analizar_datos(lista_datos):
    suma, promedio, cantidad = obtener_estadisticas(lista_datos)
    print("Suma: ", suma)
    print("Promedio: ", promedio)
    print("Cantidad: ", cantidad)
    
    
analizar_datos([1,2,4,5,6,7,29])