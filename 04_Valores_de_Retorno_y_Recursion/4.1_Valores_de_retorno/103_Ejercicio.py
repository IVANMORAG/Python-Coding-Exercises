"""
EJERCICIO 103:
Define una función obtener_mayor_de_tres que retorne el mayor de 
tres números. Luego úsala para encontrar el mayor de 6 números.

Descripción: 
Reutilizar función que retorna valor.
"""

def obtener_mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
    
def mayor_de_seis(a,b,c,d,e,f):
    mayor_grupo1 = obtener_mayor_de_tres(a,b,c)
    mayor_grupo2 = obtener_mayor_de_tres(d,e,f)
    
    return obtener_mayor_de_tres(mayor_grupo1, mayor_grupo2, 0)

print(mayor_de_seis(2,4,5,7,8,9))