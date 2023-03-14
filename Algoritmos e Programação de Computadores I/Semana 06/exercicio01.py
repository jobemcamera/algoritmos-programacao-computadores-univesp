"""
Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois exiba na tela, uma por linha, 
todas as strings de quatro letras nessa lista.
>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote
"""

lista = []

for i in range(4):
    palavra = input("Digite uma palavra: ")
    lista.append(palavra)

for j in lista:
    if len(j) == 4:
        print(j)
