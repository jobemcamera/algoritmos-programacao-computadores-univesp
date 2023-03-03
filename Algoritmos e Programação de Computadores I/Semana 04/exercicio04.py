"""
Exercício 3.10
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os valores negativos na lista. A função não deverá retornar nada.
    negatives([4, 0, −1, −3, 6, −9])
-1
-3
-9
"""

lista = []

def retornaNegativos():
    for i in range(6):
        numero = int(input("Digite um número: "))
        if numero < 0:
            lista.append(numero)
    for i in range(len(lista)):
        print(lista[i])

retornaNegativos()