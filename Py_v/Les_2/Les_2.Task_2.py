# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# https://drive.google.com/file/d/1sodBgEvusUbMxrKmnxLho0LCpEyOaZSn/view?usp=sharing


number = input('Введите натуральное число: ')
a = 0
b = 0
for n in number:
    if int(n) % 2 == 0:
        a += 1
    else:
        b += 1

print(f'кол-во четных цифр - {a}, кол-во нечестных чисел - {b}')

