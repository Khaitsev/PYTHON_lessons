# 1.В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START = 2
FINISH = 99

START_R = 2
FINISH_R = 9


def func(x):
    count = 0
    print(f'Числа кратные {x}')
    for n in range(START, FINISH):
        if n % x == 0:
            count += 1
            print(n)
    return f'Общее количество - {count} \n**********************************\n\n'


for a in range(START_R, FINISH_R):
    print(func(a))


