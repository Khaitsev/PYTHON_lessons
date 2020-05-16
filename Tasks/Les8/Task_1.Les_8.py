class Date:
    def __init__(self, date_d, date_m, date_y):
        self.date_d = date_d
        self.date_m = date_m
        self.date_y = date_y

    def __str__(self):
        return f'{self.date_d:02}-{self.date_m:02}-{self.date_y}'

    @classmethod
    def method(cls, date_d, date_m, date_y):
        try:
            return cls(int(date_d), int(date_m), int(date_y))
        except ValueError:
            if date_d.isdigit() == bool(False):
                print(f'{date_d}')
            elif date_m.isdigit() == bool(False):
                print(f'{date_m}')
            elif date_y.isdigit() == bool(False):
                print(f'{date_y}')
            quit()

    @staticmethod
    def new_try(date_d, date_m, date_y):
        if date_d > 31 or date_d < 0:
            yield 'Укажите число с 1 по 31'
        else:
            yield str(date_d)
        if date_m > 12 or date_m < 0:
            yield 'Укажите месяц с 1 по 12'
        else:
            yield str(date_m)
        if date_y <= 1800:
            yield 'Год должен быть больше 1800'
        else:
            yield str(date_y)


z = Date.method(44, 4, 23)
print(z)
a = 44, 4, 23
a = list(Date.new_try(30, 4, 1900))
print(a)
b = Date.method(a[0], a[1], a[2])
print(b)
