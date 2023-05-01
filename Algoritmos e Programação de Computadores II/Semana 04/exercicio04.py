# Implementar um programa de gerenciamento de duas filas em um banco: prioritária e normal.
# Seu programa deverá permitir que pessoas sejam inseridas no fim de cada fila, dependendo da idade de cada uma (acima de 60 anos entra na fila prioritária).
# A saída de pessoas da fila deve ocorrer da seguinte forma: a cada duas pessoas que saem da fila prioritária, uma sai da fila normal.

class Fila():
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def inserir(self, x):
        self.data.append(x)

    def remover(self):
        if len(self.data) > 0:
            return self.data.pop(0)

    def top(self):
        if len(self.data) > 0:
            return self.data[0]

    def empty(self):
        return not len(self.data) > 0
    

fila1 = Fila() # Fila prioritária 
fila2 = Fila() # Fila convencional

for i in range(10):
    idade = int(input("Informe a idade: "))
    
    if idade < 60:
        fila2.inserir(idade)
    else:
        fila1.inserir(idade)

print("Fila prioritária: ", fila1)
print("Fila convencional: ", fila2)
