def binary_search(A, key, l, r):
    if l > r:
        return -1
    else:
        m = (l + r) // 2
        if key == A[m]:
            return m
        elif key < A[m]:
            return binary_search(A, key, l, m - 1)
        elif key > A[m]:
            return binary_search(A, key, m + 1, r)
    return -1


A = [11, 21, 42, 93, 102, 203]
res = binary_search(A, 203, 0, len(A)-1)
print("res: ", res)
