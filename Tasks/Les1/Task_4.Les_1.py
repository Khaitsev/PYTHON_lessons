print('Задание 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. '
      '\nДля решения используйте цикл while и арифметические операции.')

number = int(input('Введите число: '))
b = 0

while number > 0:
    m = number % 10
    if m > b:
       b = m
    number = number // 10

print(b)
