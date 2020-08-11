# 6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

rep = (int(input('Введите номер буквы с 1 - 26: '))-1)

print(string.ascii_lowercase[rep])