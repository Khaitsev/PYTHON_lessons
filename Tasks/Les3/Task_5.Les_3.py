b = []
z = ''


def func(*args):
    a = args[0]
    global b
    for n in a:
        try:
            b.append(int(n))
        except ValueError:
            z = input('Вы ввели символ или поставили лишний пробел, если хотите продолжить - нажмите z: ')
            if z == 'z':
                print(func(input('Введите числа с пробелами: ').split(' ')))
            else:
                print('Программа завершена')
                exit()
    c = sum(b)
    print(c)
    print(func(input('Введите числа с пробелами: ').split(' ')))


print(func(input('Введите числа с пробелами: ').split(' ')))
