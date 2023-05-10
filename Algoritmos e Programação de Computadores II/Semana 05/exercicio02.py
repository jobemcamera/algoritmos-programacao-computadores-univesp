# Ordenação

# Insertion sort

def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i - 1

        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1

        v[j+1] = x

    return v

v = [35,65,2,48,10]
print(insertion_sort(v))