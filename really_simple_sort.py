# -*- coding: UTF-8 -*-
def really_simple_sort(seq):
    k = 0
    for i in range(len(seq)):
        if seq[i] == 1:
             k = k + 1
    for i in range(0, k):
        seq[i] = 1
    for i in range(k, len(seq)):
        seq[i] = 2
    return seq

if __name__ == '__main__':
    seq = [3, 4, 5, 6, 1, 2, 1, 4, 5, 8]
    print really_simple_sort(seq)
