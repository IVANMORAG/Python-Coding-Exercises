"""
EJERCICIO 165:
Crea una función es_prefijo que retorne True si el primer string
es prefijo  segundo.

Descripción:
Comparación de subcadenas al inicio.
"""

def es_prefijo(prefijo, texto_completo):
    
    if len(prefijo) > len(texto_completo):
        return False
    
    return texto_completo[:len(prefijo)] == prefijo

print(es_prefijo("Hola", "Hola mundo"))