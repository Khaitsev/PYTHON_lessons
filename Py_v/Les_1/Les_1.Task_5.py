# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.

import string

rep_sym_1 = str(input('Введите первую букву (a-y): '))
rep_sym_2 = str(input('Введите вторую букву (b-z): '))

rep_sym_1_index = (string.ascii_lowercase.index(rep_sym_1))+1  # положение в алфавите первой буквы
rep_sym_2_index = (string.ascii_lowercase.index(rep_sym_2))+1  # положение в алфавите второй буквы

rep_dif = rep_sym_2_index - rep_sym_1_index - 1  # количество букв между выбранными

print(f'положение в алфавите первой буквы - {rep_sym_1_index}, '
      f'положение в алфавите второй буквы - {rep_sym_2_index}, '
      f'количество букв между выбранными - {rep_dif}')
