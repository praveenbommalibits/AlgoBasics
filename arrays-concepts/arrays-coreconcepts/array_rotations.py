""""
Array rotations :
left rotation : first indices will be moving to end
right rotation: last indices will be moving to start


Approach 1:
Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n =7
1) Store the first d elements in a temp array
   temp[] = [1, 2]
2) Shift rest of the arr[]
   arr[] = [3, 4, 5, 6, 7, 6, 7]
3) Store back the d elements
   arr[] = [3, 4, 5, 6, 7, 1, 2]

Approach2:

"""

import array


def print_result(arr_input):
    for i in range(len(arr_input)):
        print("%d" % arr_input[i], end=" ")


# approach 1
def left_rotation_byone(arr_input, n):
    temp = arr_input[0]
    for i in range(n - 1):
        arr_input[i] = arr_input[i + 1]
    arr_input[n - 1] = temp


# approach 1
def left_rotation(arr_input, n, d):
    for i in range(d):
        left_rotation_byone(arr_input, n)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd1(a, b):
    while (b):
        a, b = b, a % b
    return a


def left_rot_approach2(arr_input, n, d):
    gcd = gcd1(n, d)
    for i in range(gcd):
        temp = arr_input[i]  # store ref value
        j = i  # store ref index
        while True:
            k = j + d  # getting the index of next rotation
            if k >= n:
                k = k - n
            if k == i:
                break
            arr_input[j] = arr_input[k]
            j = k
        arr_input[j] = temp


def reverse_arr(arr_input, start, end):
    while start < end:
        temp = arr_input[start]
        arr_input[start] = arr_input[end]
        arr_input[end] = temp
        start += 1
        end -= 1


def reverse_rotate(arr_input, d, n):
    if d == 0:
        return
    d = d % n
    reverse_arr(arr_input, 0, d-1)
    reverse_arr(arr_input, d, n-1)
    reverse_arr(arr_input, 0, n-1)


arr_input = array.array('i', [1, 2, 3, 4, 5, 6, 7])
left_rotation(arr_input, len(arr_input), 3)
print_result(arr_input)
print("\r")
arr_input = array.array('i', [1, 2, 3, 4, 5, 6, 7])
left_rot_approach2(arr_input, len(arr_input), d=3)
print_result(arr_input)
print("\r")
arr_input = array.array('i', [1, 2, 3, 4, 5, 6, 7])
reverse_rotate(arr_input, d=3, n=len(arr_input))
# approach3: left rotation by reverse
print_result(arr_input)
