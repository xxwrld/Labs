import math
a = input('Введіть елементи :').split(' ')
a = [float(el) for el in a]
a1_len = len(a)
a = [el for el in a if math.fabs(el) > 1]
a2_len = len(a)
b = [0] * (a1_len - a2_len)
a.extend(b)
print("Результат :", a)