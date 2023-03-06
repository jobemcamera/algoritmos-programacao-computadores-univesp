"""
Faça um programa em Python que leia duas
notas N1 e N2 de um aluno, e informe se ele
foi aprovado ou não numa disciplina.
Considere que a média final é dada pela
equação:
média = 0.4 * N1 + 0.6 * N2
E que o aluno está aprovado se a média for
maior ou igual a 5.0, e reprovado caso
contrário.
"""

n1 = float(input("Digite a sua nota N1: "))
n2 = float(input("Digite a sua nota N2: "))

media = round((0.4 * n1 + 0.6 * n2), 2)

print("Sua nota N1:", n1)
print("Sua nota N2:", n2)

if media >= 5:
    print("Aprovado! Sua média é:", media)
else:
    print("Reprovado! Sua média é:", media)