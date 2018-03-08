# -*- coding: UTF-8 -*-
def selection_sort(seq):
    for i in range(len(seq)-1):
        smallest = i
        for j in range(i+1, len(seq)):
            if seq[j] < seq[smallest]:
                m = seq[smallest]
                seq[smallest] = seq[j]
                seq[j] = m
    return seq

if __name__ == '__main__':
    seq = [12, 23, 14, 56, 26, 88, 34, 44]
    print selection_sort(seq)