def multyply(x, y):
    return [el * y for el in x]


def adition(x, y):
    k = []
    for i in range(len(x)):
        k.append(x[i] + y[i])
    return k


def subtraction(x, y):
    k = []
    for i in range(len(x)):
        k.append(x[i] - y[i])
    return k


a = list(map(float, input('Введіть координати вектора A: ').split(' ')))
b = list(map(float, input('Введіть координати вектора B: ').split(' ')))
c = list(map(float, input('Введіть координати вектора C: ').split(' ')))

e = subtraction(a, adition(multyply(b, 3), multyply(c, 2)))
print(e)
