"""
Arrays basics code block to handy over the further level
"""

import array

# initializing the array with array value
arr = array.array('i', [1, 2, 3])

print("The array is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print("\r")

arr.append(4)
print("The array after append is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print("\r")

arr.insert(2, 5)
print("The array after insert is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")
arr.pop(2)
print("The array after pop is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")
arr.remove(1)
print("The array after remove is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\r")
arr.reverse()
print("The array reverse is: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("array index of 2 is : ", arr.index(2))







