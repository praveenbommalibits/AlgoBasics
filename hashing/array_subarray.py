# Task: find ab array is subset of another array


def partition(arr, si, ei):
    x = arr[ei]
    i = (si - 1)

    for j in range(si, ei):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[ei] = arr[ei], arr[i + 1]
    return i + 1


def quick_sort(arr, si, ei):
    # partitioning index
    if si < ei:
        pi = partition(arr, si, ei)
        quick_sort(arr, si, pi - 1)
        quick_sort(arr, pi + 1, ei)


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if (mid == 0 or x > arr[mid - 1]) and (arr[mid] == x):
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    return -1


def is_subset(arr1, arr2, m, n):
    i = 0
    quick_sort(arr1, 0, m - 1)
    for i in range(n):
        if binary_search(arr1, 0, m - 1, arr2[i]) == -1:
            return 0

    return 1


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
m = len(arr1)
n = len(arr2)

if (is_subset(arr1, arr2, m, n)):
    print("arr2 is subset of arr1")
else:
    print("arr2 is not subset of arr1")
