"""
elaborar um programa em python que permita ao usuário entrar com n valores em um lista (utilizar o comando for). 
O algoritmo deve fazer a leitura da quantidade de números, que não pode ser mais do que 10. 
Depois, fazer a somatória dos valores positivos digitados e, após isso, retornar o resultado da soma.
"""

n = 11

while n > 10:
    n = int(input("Digite o número de valores da lista (n <= 10): "))

numeros = []
somatorio = 0

for i in range(n):
    valor = int(input("Digite um número: "))
    numeros.append(valor)
    if valor >= 0:
        somatorio += valor

print("A lista de números é:", numeros)
print("O somatório dos valores positivos é:", somatorio)
