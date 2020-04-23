def int_func(a):
    a = a[0].upper() + a[1:]
    return a


print(int_func('tExt'))


def int_func2(b):
    print(b)
    c = []
    for n in b:
        # вариант вывода 1
        print(int_func(n))
        # вариант вывода 2
        c.append(int_func(n))

    return c


print(int_func2(input('Введите слова с пробелами латинскими буквами в нижнем регистре: ').split(' ')))
