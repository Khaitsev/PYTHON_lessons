# 5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

numbers = [8, -20, 15, 6, -4, 2, 10, 18, -12, 7, 1]
min_ = -1000
dict_ = {}  # Ключ - число(-4), значение - позиция в массиве (5) (индекс - 4)

for n in numbers:
    if n < 0:
        if min_ < n:
            min_ = n
            dict_ = {n: numbers.index(n)+1}

print(dict_)

