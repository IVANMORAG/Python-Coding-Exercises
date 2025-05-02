"""
EJERCICIO 100:
Crea una función validar_contraseña que pida una
contraseña hasta que el usuario ingrese "secreto".

Bucle con input hasta obtener respuesta correcta.
"""

def validad_contraseña():
    contraseña = input("Ingresa la contraseña: ")
    while contraseña != "secreto":
        print("Contraseña incorrecta")
        contraseña = input("Ingresa la contraseña: ")
    print("Acceso concedido")
    
validad_contraseña()