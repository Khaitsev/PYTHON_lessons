# 6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

numbers = [8, 20, 15, 6, 4, 2, 10, 18, 12, 7, 1, 9]
max_num_ind = numbers[0]
min_num_ind = numbers[0]
print(numbers)

a = numbers[0]
b = numbers[0]

sum_ = 0

for n in numbers:
    if n > max_num_ind:
        max_num_ind = n
    elif n < min_num_ind:
        min_num_ind = n

for z in numbers:
    if a < z < max_num_ind:
        a = z
    elif b > z > min_num_ind:
        b = z

print(f'{max_num_ind} - максимальное значение, {min_num_ind} - минимальное значение ')  # для удобства вывожу
print(f'{a} - пред-максимальное значение, {b} - пред-минимальное значение ')
# вывел пред-минимальное и пред-максимальное значения)) неправильно понял задание, но оставлю здесь, жалко стирать.
# Само задание ниже.

for s in numbers:
    if s != max_num_ind and s != min_num_ind:
        sum_ += s

print(f'{sum_} - сумма чисел, находящиеся между максимальным и минимальным значениями')
