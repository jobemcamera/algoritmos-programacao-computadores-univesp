# Busca Binária
import random


def busca_binaria(l, x, inicio, fim):
    meio = (inicio + fim) // 2

    if fim < inicio:
        return -1
    if x == l[meio]:
        return meio
    if x < l[meio]:
        return busca_binaria(l, x, inicio, meio - 1)
    if x > l[meio]:
        return busca_binaria(l, x, meio + 1, fim)


l = random.sample(range(100), 20)
l.sort()
print("Lista:", l)

num = int(input("Número a buscar: "))

resultado_busca = busca_binaria(l, num, 0, len(l)-1)

if resultado_busca != -1:
    print("O índice do número",num,"é",resultado_busca)
else:
    print("O número",num,"não foi encontrado.")
