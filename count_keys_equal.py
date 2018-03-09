# -*- coding: UTF-8 -*-
def count_keys_equal(seq, m):
    equal = []
    for i in range(m+1):
        equal.append(0)
    for i in range(len(seq)):
        key = seq[i]
        equal[key] = equal[key] + 1
    return equal

if __name__ == '__main__':
    seq = [4, 1, 5, 0, 1, 6, 5, 1, 5, 3]
    print count_keys_equal(seq, 7)