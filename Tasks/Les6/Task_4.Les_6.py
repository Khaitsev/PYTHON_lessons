class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car has gone')

    def stop(self):
        print('Car has stopped')

    def turn(self, direction):

        if direction == 'left':
            print('The car turns to the left')
        elif direction == 'right':
            print('The car turns to the right')
        else:
            print('You direction is not correct, please sure that direction is only "right" or "left"')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print('Your speed is too high. Please drive slower. Max allowed speed is 60')


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print('Your speed is too high. Please drive slower. Max allowed speed is 40')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


try:
    b = WorkCar(80, 'blue', 'Bird')
    b.show_speed()
    b.stop()

    p = PoliceCar(99, 'red', 'Rolf')
    p.turn('left')
    p.show_speed()

    s = SportCar(190, 'red', 'Dragon')
    s.show_speed()
    s.go()

    a = Car(60, 'green', 'Ban', True)
    a.turn('right')
except TypeError:
    print('You should choose "right" or "left" in direction request')
