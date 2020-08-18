# 4.Определить, какое число в массиве встречается чаще всего.

numbers = [8, 20, 1, 15, 6, 4, 2, 8, 15, 10, 18, 8, 12, 7, 20, 8, 1]
count = 0
dic_num_count = {}  # ключ (8) - сама цифра, значение (4) - частота, с которой эта цифра встретилась

for n in set(numbers):
    if numbers.count(n) > count:
        count = numbers.count(n)
        dic_num_count = {n: numbers.count(n)}

print(dic_num_count)
