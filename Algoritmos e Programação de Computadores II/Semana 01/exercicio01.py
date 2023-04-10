# Problema Prático 3.14

# Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar nada.

# >>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']

# >>> trocaPU(ingredientes)

# >>> ingredientes

# ['maçãs', 'açúcar', 'manteiga', 'farinha']


def trocaPU(list):
    list[0] = 'maçãs'
    list[len(list)-1] = 'farinha'


ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
print(ingredientes)
trocaPU(ingredientes)
print(ingredientes)

# Listas são MUTÁVEIS