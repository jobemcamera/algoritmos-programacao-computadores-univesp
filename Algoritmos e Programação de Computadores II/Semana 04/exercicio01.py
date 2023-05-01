# Pilhas

class Pilha():
    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    def empty(self):
        return not len(self.data) > 0


p = Pilha()

p.push(4)
p.push(5)
p.push(6)

print(p)

p.pop()

print(p)
