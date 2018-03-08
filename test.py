# -*- coding: UTF-8 -*-
def partition(seq, p, r):
    q = p
    for u in range(p, r):
        if seq[u] <= seq[r]:
            seq[u], seq[q] = seq[q], seq[u]
            q = q + 1
    seq[q], seq[r] = seq[r], seq[q]
    return q

def quick_sort(seq, p, r):
    if p >= r:
        return seq
    else:
        q = partition(seq, p, r)
        quick_sort(seq, p, q)
        quick_sort(seq, q+1, r)
        return seq

if __name__ == '__main__':
    seq = [12, 7, 14, 9, 10, 11]
    print quick_sort(seq, 0, 5)