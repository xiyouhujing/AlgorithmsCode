# -*- coding: UTF-8 -*-
def insertion_sort(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        j = i - 1
        while j >= 0:
            if seq[j] > key:
                seq[j+1] = seq[j]
                seq[j] = key
            j = j -1
    return seq

if __name__ == '__main__':
    seq = [12, 3, 56, 43, 27, 59, 84, 15]
    print insertion_sort(seq)