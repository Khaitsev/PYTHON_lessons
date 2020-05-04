from time import sleep


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 3}

    def running(self):
        while True:
            print(f"Stop! Now it's {TrafficLight.__color.get(self, 'red')} color. "
                  f"Wait for {TrafficLight.__color['red']} seconds.")
            sleep(TrafficLight.__color['red'])
            print(f"Be ready! it's {TrafficLight.__color.get(self, 'yellow')} color. "
                  f"Attention! It's {TrafficLight.__color['yellow']} seconds to changing the light.")
            sleep(TrafficLight.__color['yellow'])
            print(f"Go-Go-Go! it's {TrafficLight.__color.get(self, 'green')}! "
                  f"You have {TrafficLight.__color['green']} seconds.")
            sleep(TrafficLight.__color['green'])
            print(f"Be ready! it's {TrafficLight.__color.get(self, 'yellow')} color. "
                  f"Attention! It's {TrafficLight.__color['yellow']} seconds to changing the light.")
            sleep(TrafficLight.__color['yellow'])


a = TrafficLight()
a.running()
