# -*- coding: UTF-8 -*-
def count_keys_less(equal, m):
    less = []
    for i in range(m):
        less.append(0)
    for j in range(1, m):
        less[j] = less[j-1] + equal[j-1]
    return less

if __name__ == '__main__':
    equal = [1, 3, 0, 1, 1, 3, 1, 0]
    print count_keys_less(equal, 7)