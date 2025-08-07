"""
EJERCICIO 199:
Escribe una función  procesar_lineas que tome un texto con multiples
lineas y retorne una lista de palabras de todas las líneas.

Descripión.
Combinar split() de líneas y palabras.
"""

"""
EJERCICIO 199:
Escribe una función procesar_lineas que tome un texto con múltiples
líneas y retorne una lista de palabras de todas las líneas.

Descripción:
Combinar split() de líneas y palabras.
"""

def procesar_lineas(texto):
    palabras = []
    lineas = texto.split('\n') 
    
    for linea in lineas:
        if linea.strip(): 
            palabras.extend(linea.split()) 
    
    return palabras

texto = """
Messi is the goat!
I love you Messi
and i love the tacos.
"""

print(procesar_lineas(texto))