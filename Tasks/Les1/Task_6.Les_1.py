print('Задание 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. '
      '\nКаждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, '
      '\nна который общий результат спортсмена составить не менее b километров. Программа должна принимать значения '
      '\nпараметров a и b и выводить одно натуральное число — номер дня.')

d = 1
km = 2
print(f'\nВ {d} день спортсмен пробежал {int(km)}км.')

while km <= 3:
    km = km * 1.1
    d += 1
    print(f'В {d} день спортсмен пробежал {km:.2}км.')
