"""
Tendo como dados de entrada a altura e o
sexo de uma pessoa, construa um
programa em Python que calcule seu peso
ideal, utilizando para isso as seguintes
fórmulas:
-Para homens: (72.7 * altura) – 58
-Para mulheres: (62.1 * altura) – 44.7
"""

sexo = input("Digite seu sexo (m ou f): ")
altura = float(input("Digite sua altura: "))

if sexo == "m" or sexo == "masculino":
    pesoIdeal = round((72.7 * altura) - 58, 2)
    print("Para sexo masculino, seu peso ideal é:", pesoIdeal,"kg")
elif sexo =="f" or sexo == "feminino":
    pesoIdeal = round((62.1 * altura) - 44.7, 2)
    print("Para sexo feminino, seu peso ideal é:", pesoIdeal,"kg")
else: 
    print("Error!")