def func(x, y):
    if y < 0:
        y = int(y / (-1))
    print(y)
    q = x ** y

    for n in range(1, y):
        x = x * y

    return q, x


print(func(3, -3))
