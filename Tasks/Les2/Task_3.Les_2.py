reply = int(input('Введите месяц в виде цифры от 1 до 12: '))

win = [12, 1, 2]
spr = [3, 4, 5]
sum = [6, 7, 8]
out = [9, 10, 11]

# решение через list
if win.count(reply) > 0:
    print('Зима')
elif out.count(reply) > 0:
    print('Осень')
elif spr.count(reply) > 0:
    print('Весна')
elif sum.count(reply) > 0:
    print('Лето')

# решение через list+dict
seasons = {"Зима": win, "Весна": spr, "Лето": sum, "Осень": out}

for b, c in seasons.items():
    if c.count(reply) > 0:
        print(b)