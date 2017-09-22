import random

def mergeSort(array):
    if len(array) <= 1:
        return array
    middle = int(len(array) / 2)
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print(A)
B = mergeSort(A)
print(B)