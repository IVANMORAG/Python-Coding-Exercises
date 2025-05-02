"""
EJERCICIO 99:
Escrbe una función menu_simple, que muestre opciones
1. Suma, 2.Resta, y ejecute la operación elegida con dos
números.

Descripción:
Input para menú y condicionales.
"""

def menu_simple(opcion, num1, num2):
    
    print("1 para suma.\n")
    print("2 para resta.\n")
    
    opcion = input("--- ELIGA UNA OPCION ---\n")
    
    num1 = int(input("Ingese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        return f"{num1} + {num2} = {num1 + num2}"
    elif opcion == "2":
        return f"{num1} - {num2} = {num1 - num2}"
    else:
        return "No eligio una opcion valida"
    

print(menu_simple("","",""))
        
    