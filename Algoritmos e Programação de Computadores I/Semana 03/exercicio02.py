# Exercício 2.7
# Dada a lista de notas de trabalho de casa dos alunos
# >>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# escreva:
# (a) Uma instrução que muda a última nota para 4.
# (b) Uma expressão que avalia para a nota mais alta.
# (c) Uma expressão que avalia para a média das notas.

# (a)
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2];
notas[len(notas)-1] = 4;
print('Notas: ', notas);

# (b)
print('Maior média: ', max(notas));

# (c)
media = sum(notas) / len(notas);
print('A média é: ', round(media,2));

