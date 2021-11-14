def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key:
            return index
        index = index + 1
    return -1


A = [83, 22, 44, 11, 93]
res = linearsearch(A, 22)
print("result: ", res)