# 2.Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

num_1 = deque('1F')
num_2 = deque('3AB')
total = deque()

d = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
}

if len(num_1) > len(num_2):
    for i in range((len(num_1))-(len(num_2))):
        num_2.appendleft(0)
else:
    for i in range((len(num_2))-(len(num_1))):
        num_1.appendleft(0)
co = -1
for n in reversed(num_2):
    if str(n).isalpha() and str(num_1[co]).isalpha():
        total.appendleft(int(d[n]) + int(d[num_1[co]]))
    elif str(n).isalpha():
        total.appendleft(int(d[n]) + int(num_1[co]))
    elif str(num_1[co]).isalpha():
        total.appendleft(int(n) + int(d[num_1[co]]))
    else:
        total.appendleft(int(n) + int(num_1[co]))
    co = co - 1

print(total)
p = 0
count = 1
for i in reversed(total):
    p = p + i * count
    count *= 10

print(p)
