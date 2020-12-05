from math import sin
from math import cos


def funcion(x):
    """
    :param x:
    :return:
    """
    if x > 3:
        return sin(x) + (sin(x) ** 2) + (sin(x) ** 3) + (sin(x) ** 4) + (sin(x) ** 5) + (sin(x) ** 6)
    else:
        c = cos(x)
        k = -1
        s = -(cos(x))
        for i in range(4):
            c = cos(c)
            k *= -1
            s += k * c
        return s


a = float(input('a = '))
b = float(input('b = '))
u = min(funcion(a), funcion(b))
print('U = {0}'.format(u))
