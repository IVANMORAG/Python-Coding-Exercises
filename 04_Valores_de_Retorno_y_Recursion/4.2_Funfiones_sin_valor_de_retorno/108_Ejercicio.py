"""
EJERCICIO 108:
Define una función mostrar_menu que imprima las opciones de un menú.
Otra Función precesar_opcion que imprma la acción elegida.

Descripción:
Funciones que solo muestran información.
"""

def mostrar_menu():
    print("1. Nuevo juego")
    print("2. Cargar juego")
    print("3. Salir")
    
def procesar_opcion(opcion):
    if opcion == 1:
        print("Iniciando nuevo juego ... ")
    elif opcion == 2:
        print("Cargando juego...")
    else:
        print("Saliendo...")
        

mostrar_menu()
procesar_opcion(2)