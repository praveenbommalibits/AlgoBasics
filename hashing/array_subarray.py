# Task: find ab array is subset of another array


def quick_sort(arr1, si, ei):
    # partitioning index
    if si < ei:
        pass


def is_subset(arr1, arr2, m, n):
    i = 0
    quick_sort(arr1, 0, m - 1)


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
m = len(arr1)
n = len(arr2)

if (is_subset(arr1, arr2, m, n)):
    print("arr2 is subset of arr1")
else:
    print("arr2 is not subset of arr1")
