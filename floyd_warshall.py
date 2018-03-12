# -*- coding: UTF-8 -*-
def floyd_warshall(G):
    pred = [[0 for n in range(len(G))] for n in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j or G[i][j] == float('inf'):
                pred[i][j] = None
            else:
                pred[i][j] = i
    for x in range(0, len(G)):
        for u in range(0, len(G)):
            for v in range(0, len(G)):
                if G[u][v] > G[u][x] + G[x][v]:
                    G[u][v] = G[u][x] + G[x][v]
                    pred[u][v] = x
    return G, pred

if __name__ == '__main__':
    G = [[0, 3, 8, float('inf')], [float('inf'), 0, float('inf'), 1], [float('inf'), 4, 0, float('inf')], [2, float('inf'), -5, 0]]
    print floyd_warshall(G)