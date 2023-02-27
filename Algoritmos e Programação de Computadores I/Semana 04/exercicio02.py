"""
Defina, diretamente no shell interativo, a função média(), que aceita dois números como entrada e retorna a média dos números. Um exemplo de uso é:
    average(2, 3.5)
    2.75
"""

def media(a,b):
    med = round((a+b)/2, 2)
    return med

nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))

print("A média é:",media(nota1, nota2))