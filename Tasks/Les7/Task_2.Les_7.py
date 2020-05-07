from abc import ABC, abstractmethod


class Cloth(ABC):
    def __init__(self, V_ov, H_suit):
        self.V_ov = V_ov
        self.H_suit = H_suit

    @abstractmethod
    def pr(self):
        print()


class Suit(Cloth):
    @property
    def fabric_s(self):
        return round(2 * self.H_suit + 0.3, 1)

    def pr(self):
        print('Абстракт Suit')


class Overcoat(Cloth):
    @property
    def fabric_ov(self):
        return round(self.V_ov / 6.5 + 0.5, 1)

    def pr(self):
        print('Абстракт Overcoat')


a = Suit(52, 180)
print(a.fabric_s)
b = Overcoat(54, 190)
print(b.fabric_ov)
