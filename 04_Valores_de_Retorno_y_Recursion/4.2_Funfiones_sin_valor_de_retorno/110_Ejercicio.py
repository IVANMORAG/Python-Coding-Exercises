"""
EJERCICIO 110:
Crea una función validar_datos que reciba edad y nombre e 
imprima mensajes de error si los datos no son validos.

Descripción:
Funcion que valida y muestra mensajes, sin retornar.
"""

def validar_datos(edad, nombre):
    if nombre != str(nombre) or edad != int(edad):
        print("Los datos no son validos")
    else:
        print("Nombre: ", nombre + "\nEdad: ", edad)
        
validar_datos("22", "Ivan")