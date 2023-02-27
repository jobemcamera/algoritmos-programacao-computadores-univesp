"""
Exercício 3.1
Implemente um programa que solicita a temperatura atual em graus Fahrenheit do usuário e exibe a temperatura em graus Celsius usando a fórmula

Seu programa deverá ser executado da seguinte forma:
>>>
Digite a temperatura em graus Fahrenheit: 50
A temperatura em graus Celsius é 10.0
"""

fahrenheit = input("Digite a temperatura em Fahrenheit: ")
celsius = round((5/9) * (int(fahrenheit) - 32),2)
print("A temperatura em graus Celsius é",celsius)