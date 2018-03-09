# -*- coding: UTF-8 -*-
def rearrange(A, less, m):
    B = range(0, len(A))
    C = []
    for j in range(m):
        C.append(less[j] + 1)
    for i in range(0, len(A)):
        key = A[i]
        index = C[key]
        B[index-1] = A[i]
        C[key] = C[key] + 1
    return B

