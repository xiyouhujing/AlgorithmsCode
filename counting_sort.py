# -*- coding: UTF-8 -*-
import count_keys_equal
import count_keys_less
import rearrange

def counting_sort(seq, m):
    equal = count_keys_equal.count_keys_equal(seq, m)
    less = count_keys_less.count_keys_less(equal, m)
    B = rearrange.rearrange(seq, less, m)
    return B

if __name__ == '__main__':
    seq = [4, 1, 5, 0, 1, 6, 5, 1, 5, 3]
    print counting_sort(seq, 7)