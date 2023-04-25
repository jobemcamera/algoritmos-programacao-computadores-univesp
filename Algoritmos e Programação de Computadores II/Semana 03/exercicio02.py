# Fatorial

def fatorial(n):
    if n == 0:
        return 1
    elif n > 0:
        resultado = n * fatorial(n-1)
        return resultado
    else:
        return 0
n = 4
print(fatorial(n))