# -*- coding: UTF-8 -*-
def linear_search(seq, x):
    for i in range(len(seq)):
        if seq[i] == x:
            return i
    else:
        return None

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5]
    result = linear_search(seq, 3)
    print result