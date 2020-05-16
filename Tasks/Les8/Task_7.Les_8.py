class Complex:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def com_numb(self):
        x = complex(self.arg1, self.arg2)
        return x

    def __add__(self, other):
        return self.arg1 + other.arg1, self.arg2 + other.arg2

    def __mul__(self, other):
        return self.arg1 * other.arg1, self.arg2 * other.arg2


a = Complex(5, 10)
b = Complex(15, 20)
print(a.com_numb()+b.com_numb())
print(a.com_numb()*b.com_numb())

