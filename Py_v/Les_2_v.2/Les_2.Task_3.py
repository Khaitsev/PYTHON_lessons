# 3.Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите число: '))

string = ''

for n in str(number):
    string = n + string

print(string)


# рекурсивный способ:


def de(x):

    if x == 0:
        return ''
    if x > 0:
        return str(x % 10) + str((de(x // 10)))


print(de(number))
