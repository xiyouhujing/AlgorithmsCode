# -*- coding: UTF-8 -*-
def merge(seq1, seq2):
    seq = []
    h = j = 0
    while h < len(seq1) and j < len(seq2):
        if seq1[h] < seq2[j]:
            seq.append(seq1[h])
            h = h+1
        else:
            seq.append(seq2[j])
            j = j+1
    if h == len(seq1):
        for i in seq2[j:]:
            seq.append(i)
    elif j == len(seq2):
        for i in seq1[h:]:
            seq.append(i)

    return seq