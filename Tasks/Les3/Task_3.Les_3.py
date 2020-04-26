def my_func(a, b, c):
    d = []
    n = 0
    e = [a, b, c]
    while n < 2:
        d.append(max(e))
        e.remove(max(e))
        n += 1
    return d


print(my_func(44, 454, 824))
