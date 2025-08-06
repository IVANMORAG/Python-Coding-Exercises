"""
EJERCICIO 162:
Crea una función es_mayor_ignorando_mayusculas que compare
dos strings sin considerar mayúsculas/minusculas.

Descripción:
Comparación case-insensitive
"""

def es_mayor_ignorando_mayusculas(texto1, texto2):
    return texto1.lower() > texto2.lower()

print(es_mayor_ignorando_mayusculas("Hola", "Mundo"))