"""
EJERCICIO 85:
Crea una función categotia_imc que calcule y clasifique 
el IMC: "Bajo peso"(<18.5), "Normal(18.5-24.9), Sobrepeso"(25-29.9),
"Obesidad"(>=30)

Descripción:
Cálculo matemático seguido de clasificación.
"""

def categoria_imc(peso, altura):
    
    imc = peso / (altura * altura)
    
    if imc < 18.5:
        return "Bajo peso"
    elif imc <= 24.9:
        return "Normal"
    elif imc <= 29.9:
        return "Sobrepeso" 
    else:
        return "Obesidad"
    
print(categoria_imc(70, 170))
    