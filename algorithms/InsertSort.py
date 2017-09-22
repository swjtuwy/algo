import random

def insertSort(nums):

    length = len(nums)

    for j in range(1, length):
        key = nums[j]
        i = j - 1
        while i > -1 and nums[i] > key:
            nums[i+1] = nums[i]
            i -= 1
        nums[i+1] = key

A = []
s = random.randint(5, 100)
for i in range(0, s):
    A.append(random.randint(0, 1000))
print(A)
insertSort(A)
print(A)