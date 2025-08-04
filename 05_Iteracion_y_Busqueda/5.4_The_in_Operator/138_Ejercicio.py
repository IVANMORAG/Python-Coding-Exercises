"""
EJERCICIO 138:
Define una función filtrar_palabras_prohibidas que reciba 
una lista de palabras y retorne solo las que no estan en una 
lista de palabras prohibidas.

Descripción:
Usar in para filtrar elementos en listas.
"""

def filtrarpalabras_prohibidas(lista):
    
    palabras_prohibidas = ["Hola", "Tacos", "Mar"]
    lista_filtrada = []
    
    for palabra in lista:
        
        if palabra not in palabras_prohibidas:
            lista_filtrada.append(palabra)
        
    return lista_filtrada

print(filtrarpalabras_prohibidas(["Pasto", "Tacos", "Mar"]))
            