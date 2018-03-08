# -*- coding: UTF-8 -*-
import Merge
def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        q = len(seq) // 2
        left = merge_sort(seq[:q])
        right = merge_sort(seq[q:])
        return Merge.merge(left, right)

if __name__ == '__main__':
    seq = [12, 9, 3, 7, 14, 11, 6, 2, 10, 5]
    print merge_sort(seq)
