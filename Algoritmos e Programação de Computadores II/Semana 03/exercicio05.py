# Memoização

# dict() = Dicionário em Python é uma coleção de dados sem ordem onde cada elemento possui um par chave/valor.

m = dict()


def fat(n):
    if n == 0:
        return 1
    elif m.get(n) != None:
        return m[n]
    else:
        m[n] = n * fat(n-1)
    return m[n]

print(fat(5))