print('Задание 3. Узнайте у пользователя число n. Найдите сумму чисел '
      '\n n + nn + nnn. Например, пользователь ввёл число 3. '
      'Считаем 3 + 33 + 333 = 369.')
n = input('Введите любое чило и я посчитаю в формате n + nn + nnn: ')
b = (n + n)
c = (n + n + n)

result = int(int(n) + int(b) + int(c))
print(result)