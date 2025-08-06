"""
EJERCICIO 163:
Define una función ordenar_tres_palabras que reciba tres 
strings y los retorne en orden alfabetico.

Descripción:
Ordenamiento manual usando comparaciones.
"""

def ordenar_tres_palabras(uno, dos, tres):
    
    if uno > dos and dos > tres:
        return uno, dos, tres
    elif uno > dos and tres > dos:
        return uno, tres, dos
    elif dos > uno and uno > tres:
        return dos, uno, tres
    elif dos > uno and tres > uno:
        return dos, tres, uno
    elif tres > dos and dos > uno:
        return tres, dos, uno
    elif tres > uno and uno > dos:
        return tres, uno, dos
    else:
        return False
    
print(ordenar_tres_palabras("one", "two", "three"))
        