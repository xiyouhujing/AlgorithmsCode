# -*- coding: UTF-8 -*-
def compute_transform_tables(X, Y, cc, cr, cd, ci):
    m = len(X)
    n = len(Y)
    cost = [[0 for i in range(n+1)] for j in range(m+1)]
    op = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        cost[i][0] = i * cd
        op[i][0] = 'del %s' % X[i-1]
    for j in range(1, n+1):
        cost[0][j] = j * ci
        op[0][j] = 'ins %s' % Y[j-1]
    for i in range(0, m):
        for j in range(0, n):
            if X[i] == Y[j]:
                cost[i+1][j+1] = cost[i][j] + cc
                op[i+1][j+1] = 'copy %s' % X[i]
            else:
                cost[i+1][j+1] = cost[i][j] + cr
                op[i+1][j+1] = 'rep %s' % X[i]
            if cost[i][j+1] + cd < cost[i+1][j+1]:
                cost[i+1][j+1] = cost[i][j+1] + cd
                op[i+1][j+1] = 'del %s' % X[i]
            if cost[i+1][j] + ci < cost[i+1][j+1]:
                cost[i+1][j+1] = cost[i+1][j] + ci
                op[i+1][j+1] = 'ins %s' % Y[j]
    return cost, op

if __name__ == '__main__':
    X = 'ACAACG'
    Y = 'CCGT'
    cc = -1
    cr = 1
    cd = 2
    ci = 2
    print compute_transform_tables(X, Y, cc, cr, cd, ci)