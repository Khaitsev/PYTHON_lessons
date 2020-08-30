# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import timeit

ARRAY = []
ARR_LEN = 15
FROM = -100
TO = 100

while len(ARRAY) < ARR_LEN:
    ARRAY.append(random.randrange(FROM, TO))
print(ARRAY)

# Стандартное решение пузырьком - 0.48543010000000003
"""def so(arr):
    i = 1
    while i < len(arr):
        for n in range(len(arr) - 1):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
        i += 1
    return arr"""

# Решение оптимизированное (одновременное наполнение двух краев - минимальных значений и максимальных.
# оно немного быстрее стандартного - 0.4545029
"""def so(arr):
    i = 1
    while i < (len(arr) / 2):
        for n in range(len(arr) - 1):
            if arr[n] > arr[n + 1]:
                arr[n], arr[n + 1] = arr[n + 1], arr[n]
            k = n + 1
            if arr[-k] < arr[-k - 1]:
                arr[-k], arr[-k - 1] = arr[-k - 1], arr[-k]
        i = i + 1
    return arr"""


# Третье решение с двумя циклами for и без While. Так же, перебор с двух торон.
# Все таки перебор For - не самый быстрый инструмент.
# Этот вариант медленнее всех - 0.5837719

def so(arr):
    for n in range(len(arr) - 1):
        if arr[n] > arr[n + 1]:
            arr[n], arr[n + 1] = arr[n + 1], arr[n]
        for i in range(1, len(arr)):
            if arr[-i] < arr[-i - 1]:
                arr[-i], arr[-i - 1] = arr[-i - 1], arr[-i]

    return arr


print(so(ARRAY))
print(timeit.timeit('so(ARRAY)', number=10000, globals=globals()))  # 0.5691349000000001
