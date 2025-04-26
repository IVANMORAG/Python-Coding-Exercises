"""
EJERCICIO 86:
Escribe una función acceso_sistema que verifique usuario 
y contraseña. Solo si el usuario es "admin", verifica si la 
contraseña es "1234".

Descripción:
if-anidado, primera condición determina si evaluar la segunda.
"""

def acceso_sistema(usuario, contraseña):
    if usuario == "admin":
        if contraseña == "1234":
            return "Login Exitoso"
        else:
            return "Contraseña incorrecta"
    else:
        return "Usuario incorrecto"
    
print(acceso_sistema("admin", "123"))
            