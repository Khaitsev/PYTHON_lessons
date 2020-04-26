from functools import reduce

my_list = [n for n in range(100, (1000 + 1)) if n % 2 == 0]
print(my_list)
print(reduce(lambda x, y: x * y, my_list))
