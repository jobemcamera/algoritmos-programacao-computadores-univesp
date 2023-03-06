"""
Dados três valores positivos, A, B e C,
construir um programa em Python que
verifica se os mesmos podem ser os
comprimentos dos lados de um triângulo.
Se forem, verificar e imprimir se o triângulo é
equilátero, isósceles ou escaleno.
Informar se não formarem nenhum triângulo.
"""

ladoA = float(input("Informe o lado A: "))
ladoB = float(input("Informe o lado B: "))
ladoC = float(input("Informe o lado C: "))

maiorLado = max(ladoA, ladoB, ladoC)

if maiorLado < (ladoA + ladoB + ladoC - maiorLado):
    print("Os 3 lados informados formam um triângulo!")
    if ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
        print("Os lados A, B e C formam um Triângulo Equilátero!")
    elif ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("Os lados A, B e C formam um Triângulo Escaleno!")
    else:
        print("Os lados A, B e C formam um Triângulo Isósceles!")
else:
    print("Os 3 seguimentos informados NÃO formam um triângulo!")
    
