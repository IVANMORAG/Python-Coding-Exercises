"""
EJERCICIO 80:
Crea una función mensaje_longuitud que imprima
"Texto largo" si un string tiene mas de 10 caracteres, sino
"Texto corto".

Descripción:
if-else evaluando propiedades de strings
"""

def mensaje_longuitud(mensaje):
    if len(mensaje) > 10:
        print("Mensaje largo")
    else:
        print("Texto corto")
        
mensaje_longuitud("Tacos al pastor con guacamole")