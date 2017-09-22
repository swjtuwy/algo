import random

def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(A))[::-1]:
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]




A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print(A)
bubbleSort(A)
print(A)