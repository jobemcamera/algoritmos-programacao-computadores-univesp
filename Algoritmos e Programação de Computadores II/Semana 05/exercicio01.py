# Ordenação

# Bubble sort

def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if (v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]

    return v


v = [45, 68, 98, 10, 5]
print(bubble_sort(v))
