class Ex(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        data1 = int(input('Введите делимое '))
        data2 = int(input('Введите делитель '))
        if data2 == 0:
            raise Ex('На ноль делить нельзя! Введите значения еще раз:')

    except Ex as e:
        print(e)

    except ValueError:
        print("Вы ввели не число")
    else:
        print(f'Ответ: {round((data1 / data2),2)}')
        break

