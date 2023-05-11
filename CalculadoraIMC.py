#Desenvolva uma Calculadora de IMC, o programa deve pedir o peso e
#a altura ao usuario. calcular o IMC e retornar para o usuario o IMC
#e a categoria em que se encontra

# Menor que 18,5 - Abaixo do peso
# Entre 18,5 e 24,9 - Peso normal
# Entre 25 e 29,9 - Sobrepeso
# Igual ou acima de 30 - Obesidade

def calcular(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def determinar(imc):
    if imc < 18.5:
        categoria = "Abaixo do Peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    return categoria

peso   = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura"))

imc = calcular(peso, altura)

categoria = determinar(imc)

print("Seu IMC é",imc)
print("Sua categoria é",categoria)