# 2.Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

ARRAY = []
ARR_LEN = 15
FROM = 0
TO = 50

while len(ARRAY) < ARR_LEN:
    ARRAY.append(random.randrange(FROM, TO))
print(ARRAY)

arr2 = []
mid = int(len(ARRAY) / 2)

cop = ARRAY.copy()

while len(arr2) < len(ARRAY):
    for i in cop[:mid]:
        j = i
        for n in cop[:mid]:
            if j > n:
                j = n
            for k in cop[mid:]:
                if j > k:
                    j = k
        arr2.append(j)
        cop.pop(cop.index(j))
        break

print(arr2)
print(arr2[-1-1])
