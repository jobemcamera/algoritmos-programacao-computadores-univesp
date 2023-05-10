# Ordenação

# Heap sort

def heapify(v, n, i):
    """
    Transforma o array em um heap
    """
    largest = i  # Inicializa o maior como raiz
    L = 2 * i + 1  # esquerda = 2*i + 1
    R = 2 * i + 2  # direita = 2*i + 2

    # Verifica se o filho esquerdo da raiz existe e é maior que a raiz
    if L < n and v[i] < v[L]:
        largest = L

    # Verifica se o filho direito da raiz existe e é maior que a raiz
    if R < n and v[largest] < v[R]:
        largest = R

    # Muda a raiz, se necessário
    if largest != i:
        v[i], v[largest] = v[largest], v[i]  # Troca
        heapify(v, n, largest)


def heap_sort(v):
    n = len(v)

    # Constrói o heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(v, n, i)

    # Extrai os elementos um por um
    for i in range(n - 1, 0, -1):
        v[i], v[0] = v[0], v[i]  # Troca
        heapify(v, i, 0)

    return v


v = [5, 98, 56, 2, 1, 57, 100, 656, 659898, 0, -5, -65]
print(heap_sort(v))
