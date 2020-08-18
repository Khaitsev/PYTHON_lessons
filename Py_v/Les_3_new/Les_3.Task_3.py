# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

numbers = [8, 20, 15, 6, 4, 2, 10, 18, 12, 7, 1, 9]
max_num_ind = numbers[0]
min_num_ind = numbers[0]
print(numbers)

for n in numbers:
    if n > max_num_ind:
        max_num_ind = n
    elif n < min_num_ind:
        min_num_ind = n

print(f'{max_num_ind} - максимальная цифра, {numbers.index(max_num_ind)} - ее индекс', sep=', ')
print(f'{min_num_ind} - минимальная цифра, {numbers.index(min_num_ind)} - ее индекс', sep=', ')

numbers[numbers.index(min_num_ind)], numbers[numbers.index(max_num_ind)] = \
    numbers[numbers.index(max_num_ind)], numbers[numbers.index(min_num_ind)]

print(numbers)
