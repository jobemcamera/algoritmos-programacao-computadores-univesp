"""
Exercício 4.2
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:
(a) A variável cont, a quantidade de ocorrências da string 'day' na string previsão.
(b) A variável clima, o índice em que a substring 'sunny' começa.
(c) A variável troca, uma cópia de previsão na qual cada ocorrência da substring 'sunny' é substituída por 'cloudy'.
"""

previsao = "It will be a sunny day today"

# (a)
count = 0
for i in range(0,len(previsao)):
    if previsao[i] == 'd':
        if previsao[i+1] == 'a':
            if previsao[i+2] == 'y':
                count += 1
# 
print("A string 'day' ocorre",count,"vezes.")

# (b)
clima = 0
for j in range(0,len(previsao)):
    if previsao[j] == 's':
        if previsao[j+1] == 'u':
            if previsao[j+2] == 'n':
                if previsao[j+3] == 'n':
                    if previsao[j+4] == 'y':
                        clima = j

print("A substring 'sunny' começa no índice", clima)

# (c)
troca = previsao.replace('sunny', 'cloudy')
                        
print(troca)