# -*- coding: UTF-8 -*-
def sentinel_linear_search(seq, x):
    last = seq[-1]
    seq[-1] = x
    i = 0
    while seq[i] != x:
        i += 1
    seq[-1] = last
    if i < len(seq)-1 or seq[-1] == x:
        return i
    else:
        return None

if __name__ == '__main__':
    seq = [1, 2, 3, 4, 5]
    result1 = sentinel_linear_search(seq, 4)
    result2 = sentinel_linear_search(seq, 5)
    result3 = sentinel_linear_search(seq, 6)
    print result1
    print result2
    print result3