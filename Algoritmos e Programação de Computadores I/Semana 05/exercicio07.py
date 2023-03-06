"""
Exercício 5.1
Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa (em metros) e o peso (em quilos) e calcula o Índice de Massa Corporal (IMC) dessa pessoa.
Sua função deverá exibir a string 'Abaixo do peso' se o imc < 18.5, 'Normal' se 18,5 <= imc < 25, e 'Sobrepeso' se imc >= 25.
>>> meuIMC(86, 1.90)
Normal
>>> meuIMC(63, 1.90)
Abaixo do peso
"""

def meuIMC(peso, altura):
    imc = round(peso / (altura * altura), 2)
    if imc < 18.5:
        print("Abaixo do peso. IMC = ", imc)
    elif imc == 18.5 or imc < 25:
        print("Normal. IMC = ", imc)
    else:
        print("Sobrepeso. IMC = ", imc)

peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em m: "))
meuIMC(peso, altura)