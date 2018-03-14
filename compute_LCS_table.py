# -*- coding: UTF-8 -*-
def compute_LCS_table(X, Y):
    m = len(X)
    n = len(Y)
    seq = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                seq[i+1][j+1] = seq[i][j] + 1
            else:
                if seq[i+1][j] > seq[i][j+1]:
                    seq[i+1][j+1] = seq[i+1][j]
                else:
                    seq[i+1][j+1] = seq[i][j+1]
    return seq

if __name__ == '__main__':
    X = 'CATCGA'
    Y = 'GTACCGTCA'
    print compute_LCS_table(X, Y)