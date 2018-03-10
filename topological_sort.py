# -*- coding: UTF-8 -*-
def get_in_degree(D, G):# D为所有顶点集合，G为有向边集合
    in_degree = D[:]# 用来存储未被删除的入度为0的定点
    E = []
    if len(G) == 0:
        return in_degree

    for i in G:
        if i[1] in in_degree:
            in_degree.remove(i[1])
    for n in in_degree:
        D.remove(n)

    for m in G:
        if m[0] in in_degree:
            E.append(m)
    for j in E:
        G.remove(j)

    return in_degree

def topological_sort(D, G):
    in_degrees = []
    while True:
        nodes = get_in_degree(D, G)
        in_degrees.extend(nodes)
        if len(G) == 0:
            in_degrees.extend(D)
            break
    return in_degrees

if __name__ == '__main__':
    D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    G = [(1, 3), (2, 4), (3, 4), (3, 5), (4, 6), (5, 6), (6, 7), (6, 11), (7, 8), (8, 13), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14)]
    print topological_sort(D, G)