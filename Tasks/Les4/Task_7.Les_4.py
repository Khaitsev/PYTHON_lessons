from math import factorial
from functools import reduce

print(factorial(4))
a = reduce(lambda x, y: x * y, range(1, 5))
print(a)


def gen(z):
    yield factorial(z)


generator = [n for n in gen(4)]
print(generator)

