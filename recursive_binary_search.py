# -*- coding: UTF-8 -*-
def recursive_binary_search(seq, p, r, x):
    if p > r:
        return None
    else:
        q = (p + r) // 2
        if seq[q] == x:
            return q
        elif seq[q] > x:
            return recursive_binary_search(seq, p, q-1, x)
        else:
            return recursive_binary_search(seq, q+1, r, x)

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6, 7, 8]
    print recursive_binary_search(seq, 0, 7, 6)