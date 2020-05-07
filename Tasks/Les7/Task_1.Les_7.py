class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.new_matrix = []

    def __str__(self):
        for n in self.new_matrix:
            print(str(n))

    def __add__(self, other):
        for n in range(len(self.matrix)):
            try:
                self.new_matrix.append(list(map(lambda x, y: x + y, self.matrix[n], other.matrix[n])))
            except IndexError:
                print('Колличество значений матриц не совпадает.')


a = Matrix([[43, 54], [12, 11], [33, 66], [11, 22]])
b = Matrix([[41, 89], [16, 123], [58, 1], [23, 41]])
try:
    print(a + b)
    print(a)


except TypeError:
    pass
