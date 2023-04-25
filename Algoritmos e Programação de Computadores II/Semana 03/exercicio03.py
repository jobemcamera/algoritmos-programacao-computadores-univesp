# Sequência Fibonacci

def fibo(posicao):
    if posicao == 0:
        return 0
    elif posicao == 1:
        return 1
    else:
        resultado = fibo(posicao-1) + fibo(posicao-2)
        return resultado
    
posicao = 13
print(fibo(posicao))