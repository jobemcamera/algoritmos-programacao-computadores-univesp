# Herança: A class MyList herda todos os métodos da class list

import random

class MyList(list):
    def choice(self):
        return random.choice(self)
    

l = MyList([1,2,3,4,5,6])

print(len(l)) # herdado da class list
print(l.choice()) # novo método 
