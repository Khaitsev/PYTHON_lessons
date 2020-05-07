class Cell:
    def __init__(self, qty_cell):
        self.qty_cell = int(qty_cell)

    def __add__(self, other):
        return self.qty_cell + other.qty_cell

    def __sub__(self, other):
        if self.qty_cell - other.qty_cell < 0:
            return 'Результат меньше "0" - клетки исчезли'
        else:
            return self.qty_cell - other.qty_cell

    def __mul__(self, other):
        return self.qty_cell * other.qty_cell

    def __truediv__(self, other):
        return int(self.qty_cell / other.qty_cell)

    def make_order(self, qty):
        a = self.qty_cell // qty
        b = self.qty_cell % qty
        z = ''
        for n in range(1, self.qty_cell + 1):
            if n % qty == 0 and (n + qty) < self.qty_cell + 1:
                z = str(qty * '*')
                print(z)

        print(z + (b * '*'))

        quit()


a1 = Cell(35)
a2 = Cell(55)
print(a1 + a2)
print(a1 - a2)
print(a1 * a2)
print(a1 / a2)
print(a2.make_order(4))
