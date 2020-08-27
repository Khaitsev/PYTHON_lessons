# 1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно
# вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections
from collections import Counter

qty = int(input('Введите кол-во компаний: '))

d = dict()

for n in range(qty):
    comp_name = input(f'Название {n + 1}-й компании: ')

    i = float(input(f'Прибыль {comp_name} за I квартал: '))
    ii = float(input(f'Прибыль {comp_name} за II квартал: '))
    iii = float(input(f'Прибыль {comp_name} за III квартал: '))
    iv = float(input(f'Прибыль {comp_name} за IV квартал: '))
    d[comp_name] = i, ii, iii, iv

su = sum([sum(a) for z, a in d.items()])
avg = sum([sum(a) for z, a in d.items()]) / qty

Point = collections.namedtuple('Point', ['sum'])

max_ = Point(0)
min_ = Point(0)
m = 0
mi = 1000000
u = dict()

for i, z in d.items():
    if sum(z) > avg:
        u[i] = 'Доход выше среднего'
    elif sum(z) < avg:
        u[i] = 'Доход ниже среднего'
    elif sum(z) == avg:
        u[i] = 'Доход средний'
    if sum(z) > m:
        m = sum(z)
        max_ = (i, [sum(z)])
    if sum(z) < mi:
        mi = sum(z)
        min_ = (i, [sum(z)])

print(f'Сумма общей прибыли: {su}')
print(f'Средняя прибылль по всем компаниям: {avg}')
print(f'Предприятие с наибольшей прибылью: {max_}')
print(f'Предприятие с наименьшей прибылью: {min_}')
print(u)
print(Counter(u.values()))
