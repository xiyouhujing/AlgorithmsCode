# -*- coding: UTF-8 -*-
import compute_LCS_table

def assemble_LCS(X, Y, seq, i, j):
    if i - 1 < 0 or j - 1 < 0:
        return ''
    if X[i-1] == Y[j-1]:
        assemble_LCS(X, Y, seq, i-1, j-1)
        print X[i - 1]
    else:
        if seq[i][j-1] > seq[i-1][j]:
            assemble_LCS(X, Y, seq, i, j-1)
        else:
            assemble_LCS(X, Y, seq, i-1, j)

if __name__ == '__main__':
    X = 'CATCGA'
    Y = 'GTACCGTCA'
    seq = compute_LCS_table.compute_LCS_table(X, Y)
    assemble_LCS(X, Y, seq, 6, 9)