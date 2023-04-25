# Recursão x Iteração
import time

def fib_rec(n):
    if n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    res = n
    a, b = 0, 1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
    return res

n = 20
start = time.time()
print(fib_rec(n))
print('Recursivo: {} segundos'.format(time.time() - start))

start = time.time()
print(fib_it(n))
print('Iterativo: {} segundos'.format(time.time() - start))