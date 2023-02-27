"""
Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo (um número não negativo) e retorna o perímetro do círculo. 
Você deverá escrever sua implementação em um módulo chamado perímetro.py. Um exemplo de uso é:
    perimeter(1)
    6.283185307179586
"""
import math

def perimetro(raio):
    return(2 * math.pi * raio)

raio = float(input("Digite o valor do raio (r>0): "))
print("O perímetro de uma circunferência de raio",raio,"é",perimetro(raio))
