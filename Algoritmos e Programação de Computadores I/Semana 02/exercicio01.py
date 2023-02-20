# Exercício 2.1
# Escreva expressões algébricas Python correspondentes aos seguintes comandos:
# (a) A soma dos 5 primeiros inteiros positivos.
# (b) A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
# (c) O número de vezes que 73 cabe em 403.
# (d) O resto de quando 403 é dividido por 73.
# (e) 2 à 10ª potência.
# (f) O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
# (g) O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.

import math
# (a)
soma = 1+2+3+4+5
print('A soma dos 5 primeiros números inteiros é:', soma)

# (b)
sara = 23
mark = 19
fatima = 31
media = round((sara + mark + fatima) / 3, 1)
print('A média das idades de Sara, Mark e Fátima é', media,"anos.")

# (c)
numero1 = 73
numero2 = 403
quantidade = math.ceil(numero2 / numero1)
print("O número de vezes que",numero1,"cabe em",numero2,"é", quantidade)

# (d)
resto = numero2 % numero1
print("O resto da divisão de",numero2,"por",numero1,"é",resto)

# (e)
print("2 elevado a 10 é", 2**10)

# (f)
alturaSara = 54
alturaMark = 57
print("O valor absoluto da diferença de altura entre Sara e Mark é", abs(alturaMark-alturaSara))

# (g)
precos = [34.99, 29.95, 31.50]
menorPreco = min(precos)
print("O menor valor entre os valores:",precos,"é",menorPreco)