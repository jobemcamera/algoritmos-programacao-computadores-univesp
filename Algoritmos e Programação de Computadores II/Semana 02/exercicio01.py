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
    
    # x + y equivale a x.__add__(y)
    # x + y ==> (2,3) + (2,2) => (4,5)
    # x + 8 ==> (2,3) + 8 => (10,11)
    def __add__(self, other):
        if type(other) == Point:
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other, self.y + other)
        

# instanciando a classe Point() criando o objeto "p"
p = Point()
print('p:',p)

q = Point(3,4)
print('q:',q)
q.move(3,-5)
print('q.move(3,-5):',q)

g = Point(1,1)
print('g:',g)
g.get()
print('g.get():', g)

print('p+q:',p+q)
print('p+8:',p+8)
