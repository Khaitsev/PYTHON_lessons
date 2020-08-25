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
import timeit
import cProfile

"""def si(z):
    x = z * 20
    sieve = [k for k in range(x)]
    sieve[1] = 0
    res = []

    for n in range(0, x):
        if sieve[n] != 0:
            res.append(n)
            j = n + n
            while j < x:
                sieve[j] = 0
                j += n

    return str(res[z - 1])"""


# print(timeit.timeit('si(100)', number=1000, globals=globals()))  # 0.8782221
# print(timeit.timeit('si(200)', number=1000, globals=globals()))  # 1.8972007000000002
# print(timeit.timeit('si(300)', number=1000, globals=globals()))  # 2.7160465
# print(timeit.timeit('si(400)', number=1000, globals=globals()))  # 3.7773578
# print(timeit.timeit('si(500)', number=1000, globals=globals()))  # 4.7712444

# print(timeit.timeit('si(1000)', number=1000, globals=globals()))  # 9.7974401


##############################################################################


# это второй вариант кода - самый быстрый из трех (первый и третий примерно равны по скорости (коды ниже сохранил),
# хотя третий короче и оптимизированнее первых двух, как мне показалось)
def prime(x):
    numb = []
    for n in range(2, 10000000):
        if len(numb) == x + 1:
            return str(numb[x - 1])
        if n == 2:
            numb.append(n)
        else:
            for i in numb:
                if n % i != 0:
                    if i == numb[-1]:
                        numb.append(n)
                    else:
                        continue
                elif n == i or n % i == 0:
                    break


# print(timeit.timeit('prime(100)', number=1000, globals=globals()))  # первый: 1.483455; второй: 0.9129573
# print(timeit.timeit('prime(200)', number=1000, globals=globals()))  # 5.516417; 3.44439
# print(timeit.timeit('prime(300)', number=1000, globals=globals()))  # 12.8687892; 7.2932925
# print(timeit.timeit('prime(400)', number=1000, globals=globals()))  # 21.8732148; 13.1182386
# print(timeit.timeit('prime(500)', number=1000, globals=globals()))  # 37.3868616; 19.8542521

# print(timeit.timeit('prime(1000)', number=1000, globals=globals()))  # 141.7713003; 78.1952732


# cProfile.run('prime(1000)')


##########################################


# Это первый вариант кода до оптимизации!
"""def prime(x):
    numb = []
    for n in range(2, 10000000):
        if len(numb) == x + 1:
            return str(numb[x - 1])
        if n == 2:
            numb.append(n)
        else:
            for i in numb:
                if n == i:
                    break
                elif n % i == 0:
                    break
                elif n % i != 0:
                    if i == numb[-1]:
                        numb.append(n)
                    else:
                        continue"""

# это второй вариант кода - после оптимизации
"""def prime(x):
    numb = []
    for n in range(2, 10000000):
        if len(numb) == x + 1:
            return str(numb[x - 1])
        if n == 2:
            numb.append(n)
        else:
            for i in numb:
                if n % i != 0:
                    if i == numb[-1]:
                        numb.append(n)
                    else:
                        continue
                elif n == i or n % i == 0:
                    break"""

# это третий вариант кода - почему-то медленее второго
"""def prime(x):
    numb = []
    for n in range(2, 10000000):
        if len(numb) == x + 1:
            return str(numb[x - 1])
        if n == 2:
            numb.append(n)
        else:
            for i in numb:
                if n % i != 0 and i == numb[-1]:
                    numb.append(n)
                elif n % i == 0 or n == i:
                    break
                else:
                    continue"""