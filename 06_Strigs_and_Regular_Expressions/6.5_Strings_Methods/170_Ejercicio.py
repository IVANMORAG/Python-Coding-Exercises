"""
EJERCICIO 170:
Crea una función validar_formato_email que use metodos de string para 
verificar si un texto contiene  @ y ..

Descripción:
Combinar varios métodos para validación.
"""

def validar_formato_email(email):
    
    email_limpio = email.strip()
    
    tiene_arroba = "@" in email_limpio
    tiene_punto = "." in email_limpio
    
    no_esta_vacio = len(email_limpio) > 0
    
    return tiene_arroba and tiene_punto and no_esta_vacio


print(validar_formato_email("mmmm@gamil.com"))