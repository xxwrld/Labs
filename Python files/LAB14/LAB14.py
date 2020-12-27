import math
from functools import reduce
import random


def rand():
    return random.randint(1, 10)


class TBody:
    def __init__(self, *args):
        self.sides = list(map(float, args))

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, args):
        for el in args:
            if el <= 0:
                raise Exception('Must be positive!')
            else:
                self.__sides = list(map(float, args))

    def input_abc(self, *args):
        self.sides = list(map(float, args))

    def print_abc(self):
        return self.sides

    @property
    def volume(self):
        return

    @property
    def square(self):
        return


class TParallelepiped(TBody):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    @property
    def volume(self):
        return reduce(lambda d, x: d * x, super().sides)

    @property
    def square(self):
        return 2 * (self.sides[0] * self.sides[1] + self.sides[0] * self.sides[2] +
                    self.sides[1] * self.sides[2])


class TBall(TBody):
    def __init__(self, r):
        super().__init__(r)

    @property
    def r(self):
        return float(super().sides[0])

    @r.setter
    def r(self, _r):
        super().sides[0] = _r

    @property
    def volume(self):
        return (4/3) * math.pi * self.r ** 3

    @property
    def square(self):
        return 4 * math.pi * self.r ** 2


n = int(input('n = '))
f = [TParallelepiped(rand(), rand(), rand()) if rand() > 4 else TBall(rand()) for i in range(n)]
total = sum([el.square for el in f])
print(total)
