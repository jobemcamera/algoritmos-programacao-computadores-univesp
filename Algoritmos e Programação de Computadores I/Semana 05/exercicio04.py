"""
Exercício 3.2
Traduza estas instruções condicionais em instruções if do Python:
(a) Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'.
(b) Se o nome está na lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um dos 5 maiores jogadores de beisebol de todos os tempos!'.
(c) Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
(d) Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
"""

# (a)
idade = int(input("Digite sua idade: "))
if idade >= 62:
    print("Para a idade",idade,"anos ou mais, você pode obter benefícios de pensão")
else:
    print("Para a idade",idade,"anos, você não pode obter benefícios de pensão")

# (b)
nome = input("Digite o nome de um jogador de beisebol: ")
jogadores = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if nome in jogadores:
    print("O jogador",nome,"é um dos 5 maiores jogadores de beisebol de todos os tempos!")
else:
    print("O jogador",nome,"não é um dos 5 maiores jogadores de beisebol de todos os tempos!")

# (c)
golpes = int(input("Número de golpes: "))
defesa = int(input("Valor de defesa: "))
if golpes > defesa:
    print("Para",golpes,"golpes e defesa",defesa,", você está morto!")
elif golpes < defesa:
    print("Para",golpes,"golpes e defesa",defesa,", você sobreviveu!")
else:
    print("Para",golpes,"golpes e defesa",defesa,", empatou!")

# (d)
direcao = input("Informe uma direção (N, L, S, O): ")
if direcao == "N" or direcao == "L" or direcao == "S" or direcao == "O":
    print("Direção",direcao,", posso escapar!!!")
else:
    print("Direção",direcao,". Não existe essa direção, então não posso escapar!!!")