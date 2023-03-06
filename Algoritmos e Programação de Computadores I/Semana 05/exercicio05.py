"""
Exercício 3.3
Traduza estas declarações em instruções if/else do Python:
(a) Se ano é divisível por 4, exiba 'Pode ser um ano bissexto.'; caso contrário, exiba 'Definitivamente não é um ano bissexto.'
(b) Se a lista bilhete é igual à lista loteria, exiba 'Você ganhou!'; se não, exiba 'Melhor sorte da próxima vez…'.
"""

# (a)
ano = int(input("Informe o ano: "))
if ano % 4 == 0:
    print("O ano", ano, "é um ano bissexto.")
else: 
    print("O ano", ano, "não é um ano bissexto.")

# (b)
loteria = 55
bilhete = int(input("Digite o valor do bilhete: "))
if bilhete == loteria:
    print("Você ganhou!!! O número sorteado era",loteria,"mesmo.")
else:
    print("Melgor sorte da próxima vez... O número sorteado era",loteria)