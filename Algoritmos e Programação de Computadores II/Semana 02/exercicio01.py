class Point:
    # self, por padrão, referencia ao próprio objeto
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def get(self):
        return self.x, self.y
    
    def move(self, offsetx, offsety):
        self.x += offsetx
        self.y += offsety

    def __repr__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

# instanciando a classe Point() criando o objeto "p"
p = Point()
print(p)

q = Point(3,4)
print(q)
q.move(3,-5)
print(q)

g = Point(1,1)
print(g)
g.get()
print(g)

