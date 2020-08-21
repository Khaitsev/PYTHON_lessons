# 1.Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
# для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.


# Вывод: работать с массивами(3) дольше, чем со строками(1). Рекурсия(2) показала себя быстрее всех,
# с небольшим отрывом от строк(1).


import timeit
import cProfile

# I.

number = 55533399


def string_(x):
    string = ''
    if number > 0:
        for n in str(x):
            string = n + string
        return string


print(string_(number))
print(timeit.timeit(string_(number), number=1000000))  # 1. 0.011047300000000003
print(timeit.timeit(string_(number*11), number=1000000))  # 2. 0.010446300000000006
print(timeit.timeit(string_(number*22), number=1000000))  # 3. 0.010151300000000002
print(timeit.timeit(string_(number*33), number=1000000))  # 4. 0.010214

cProfile.run(string_(number))


# II.

def de(x):
    if x == 0:
        return ''
    if x > 0:
        return str(x % 10) + str((de(x // 10)))


print(de(number))
print(timeit.timeit(de(number), number=1000000))  # 1. 0.0102352
print(timeit.timeit(de(number*11), number=1000000))  # 2. 0.0098742
print(timeit.timeit(de(number*22), number=1000000))  # 3. 0.010778499999999996
print(timeit.timeit(de(number*33), number=1000000))  # 4. 0.00983400000000001

cProfile.run(de(number))


# III.

def fun(x):
    rev_numb = []
    for a in list(reversed(str(x))):
        rev_numb.append(int(a))
    return str(rev_numb)


print(fun(number))
print(timeit.timeit(fun(number), number=1000000))  # 1. 0.0839511
print(timeit.timeit(fun(number*11), number=1000000))  # 2. 0.08800809999999998
print(timeit.timeit(fun(number*22), number=1000000))  # 3. 0.08914419999999995
print(timeit.timeit(fun(number*33), number=1000000))  # 4. 0.08715860000000003

cProfile.run(fun(number))
