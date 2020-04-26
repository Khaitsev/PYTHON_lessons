def my_func(a, b):
    try:
        c = a / b
        c = round(c, 2)
        return c
    except ZeroDivisionError:
        print('на ноль делить нельзя')
        return my_func(a=int(input('ведите 1 число: ')), b=int(input('ведите 2 число: ')))


print(my_func(a=int(input('ведите 1 число: ')), b=int(input('ведите 2 число: '))))
