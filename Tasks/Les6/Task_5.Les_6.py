class Stationery:
    def __init__(self, title):
        title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print('Красим маркером')


a = Stationery('класс')
a.draw()

pen = Pen('Ручка')
pen.draw()

pencil = Pencil('Карандаш')
pencil.draw()

handle = Handle('Фламастер')
handle.draw()
