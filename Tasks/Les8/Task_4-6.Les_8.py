class Warehouse:
    printer = []
    scanner = []
    xerox = []
    totally = []

    @staticmethod
    def total(branch):
        for tots in Warehouse.printer, Warehouse.scanner, Warehouse.xerox:
            tot = {'отдел': '', 'принтеры': 0, 'сканеры': 0, 'ксероксы': 0}
            tot['отдел'] = branch
            for n in tots:
                if n['отдел'] == branch:
                    tot['принтеры'] = tot['принтеры'] + n['кол-во']
                    tot['сканеры'] = tot['сканеры'] + n['кол-во']
                    tot['ксероксы'] = tot['ксероксы'] + n['кол-во']
        Warehouse.totally.append(tot)


class Equip:
    def __init__(self, branch):
        self.branch = branch


class Printer(Equip):
    def meth_print(self):
        while True:
            try:
                jet = int(input('Введите количесвто лазерных принтеров: '))
                inkjet = int(input('Введите количество струйных принетров: '))
                total = jet + inkjet
            except ValueError:
                print('Вы ввели неверное значение или вообще не ввели его, '
                      'повторите ввод еще раз или введите "0"')
            else:
                print(f'{total} принетров(-а) уже собираюстя.')
                Warehouse.printer.append({'наименование': 'принтер', 'отдел': self.branch, 'кол-во': total})
                break


class Scanner(Equip):
    def meth_scan(self):
        while True:
            try:
                multifunc = int(input('Введите количесвто мультифункциональных устрйств: '))
                scanner_single = int(input('Введите количество сканнеров: '))
                total = multifunc + scanner_single
            except ValueError:
                print('Вы ввели неверное значение или вообще не ввели его, '
                      'повторите ввод еще раз или введите "0"')
            else:
                print(f'{total} сканеров(-а) уже собираюстя.')
                Warehouse.scanner.append({'наименование': 'сканер', 'отдел': self.branch, 'кол-во': total})
                break


class Xerox(Equip):
    def meth_xer(self):
        while True:
            try:
                xerox = int(input('Введите количесвто моделей Xerox: '))
                xerox_one = int(input('Введите количество Xerox One: '))
                total = xerox + xerox_one
            except ValueError:
                print('Вы ввели неверное значение или вообще не ввели его, '
                      'повторите еще раз')
            else:
                print(f'{total} ксероксов(-а) уже собираюстя')
                Warehouse.xerox.append({'наименование': 'ксерокс', 'отдел': self.branch, 'кол-во': total})
                break


x = Printer('Firm1')
x.meth_print()
x = Scanner('Firm1')
x.meth_scan()
x = Xerox('Firm1')
x.meth_xer()

z = Printer('Firm2')
z.meth_print()
z = Scanner('Firm2')
z.meth_scan()
z = Xerox('Firm2')
z.meth_xer()

Warehouse.total(x.branch)
Warehouse.total(z.branch)
print(Warehouse.totally)
