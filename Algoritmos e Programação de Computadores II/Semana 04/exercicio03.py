# Filas

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
    

f = Fila()

f.inserir(1)
f.inserir(2)
f.inserir(3)

print(f)

f.remover()
print(f)

f.remover()
print(f)