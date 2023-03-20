# Dada a matriz M, verificar se M é uma matriz transposta.

def simetrica(M):
    num_linhas = len(M)
    num_colunas = len(M[0]) # poderia ser qual linha da matriz

    for i in range(num_linhas):
        for j in range(i + 1, num_colunas):
            if M[i][j] != M[j][i]:
                return False
    
    return True

M = [[1,2,3],
     [2,4,5],
     [3,5,3]]

print(simetrica(M))