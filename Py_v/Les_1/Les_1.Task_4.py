# Написать программу, которая генерирует в указанных пользователем границах:
# ● случайное целое число,
# ● случайное вещественное число,
# ● случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random
import string

rep_int_1 = int(input('Введите первое число: '))
rep_int_2 = int(input('Введите второе число: '))
print(f'Случайное целое число в диапазоне между {rep_int_1} и {rep_int_2} = '
      f'{random.randint(rep_int_1, rep_int_2)}')

print(f'Случайное вещественное число в диапазоне между {rep_int_1} и {rep_int_2} = '
      f'{round(random.uniform(rep_int_1, rep_int_2), 2)}')

rep_sym_1 = str(input('Введите начальную букву (a-y): '))
rep_sym_2 = str(input('Введите конечную букву (b-z): '))
random_s = (random.randrange(string.ascii_lowercase.index(rep_sym_1),
                             string.ascii_lowercase.index(rep_sym_2)))
print(f'Случайная буква в деапазоне между {rep_sym_1} и {rep_sym_2} = '
      f'{string.ascii_lowercase[random_s]}')
