# 2.Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
# принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.


"""def si(x):
    x = x * 20
    count = 0
    sieve = [k for k in range(x)]
    sieve[1] = 0
    res = []

    for n in range(2, x):
        if sieve[n] != 0:
            res.append(n)
            count += 1
            j = n + n
            while j < x:
                sieve[j] = 0
                j += n
    return res[int(x/20-1)]
    #return res


print(si(10))"""


def si(x):
    count = 0
    sieve = [k for k in range(x)]
    sieve[1] = 0
    res = []

    for n in range(2, x):
        if x <= count:
            x = x * 10
        if sieve[n] != 0:
            res.append(n)
            count += 1
            j = n + n
            while j < x:
                sieve[j] = 0
                j += n
    #return res[int(x/20-1)]
    #return res
    return count


print(si(10))
