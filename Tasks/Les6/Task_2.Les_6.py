class Road:
    __length = int()
    __width = int()

    def __init__(self):
        self.__length = int(input('Введите длину полотна: '))
        self.__width = int(input('Введите ширинку полотна: '))
        weight = 25
        thickness = 1
        result = self.__length * self.__width * weight * thickness
        print(f'{result} тонн')


a = Road()

