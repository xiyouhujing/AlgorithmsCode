# -*- coding: UTF-8 -*-
def recursive_linear_search(seq, i, x):
    if i > len(seq) - 1:
        return None
    else:
        if seq[i] == x:
            return i
        else:
            return recursive_linear_search(seq, i+1, x)

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5, 6]
    result = recursive_linear_search(seq, 0, 4)
    print result