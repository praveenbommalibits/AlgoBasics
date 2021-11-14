"""
1. Array in sorted order
2. Examine the middle element
3. If matches , return key
4. If key < middle element, search lower half
5. If key > middle element, search upper half

"""
from math import floor


def binary_search(A, key):
    l = 0
    r = len(A) - 1
    while l <= r:
        m = (l + r) // 2
        if key == A[m]:
            return m
        elif key < A[m]:
            r = m - 1
        elif key > A[m]:
            l = m + 1
    return -1


A = [33, 42, 52, 62, 93, 95]
res = binary_search(A, 612)
print("res: ", res)
