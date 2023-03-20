# Dada a matriz M, retorne sua correspondente transposta.

def transposta(M):
    num_linhas = len(M)
    num_colunas = len(M[0])

    # cria uma lista com (num_linhas) elementos iguais a zero: [0, 0, 0, ..., 0]
    M_t = [[0 for _ in range(num_linhas)] for _ in range(num_colunas)]

    for i in range(num_linhas):
        for j in range(num_colunas):
            M_t[j][i] = M[i][j]
    return M_t


M = [[1,2,3],
     [8,4,5],
     [3,6,3]]

print(transposta(M))