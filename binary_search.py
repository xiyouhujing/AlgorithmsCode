# -*- coding: UTF-8 -*-
def binary_search(seq, x):
    p = 0
    r = len(seq) - 1
    while p <= r:
        q = (p + r) // 2
        if seq[q] == x:
            return q
        elif seq[q] > x:
            r = q - 1
        else:
            p = q + 1
    return None

if __name__ == '__main__':
    lis = [11, 12, 13, 14, 16, 18, 20, 23]
    result = binary_search(lis, 20)
    print result