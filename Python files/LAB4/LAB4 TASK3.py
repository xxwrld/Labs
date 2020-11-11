from math import sqrt

x1 = float(input("Введіть х1"))
x2 = float(input("Введіть х2"))
x3 = float(input("Введіть х3"))
y1 = float(input("Введіть у1"))
y2 = float(input("Введіть у2"))
y3 = float(input("Введіть у3"))
if (-1) < (x1 + x2 + y1 + y2) / (sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))) < 0:
    print("Тупокутний")
elif (-1) < (x2 + x3 + y2 + y3) / (sqrt((x2 ** 2 + y2 ** 2) * (x3 ** 2 + y3 ** 2))) < 0:
    print("Тупокутний")
elif (-1) < (x1 + x3 + y1 + y3) / (sqrt((x1 ** 2 + y1 ** 2) * (x3 ** 2 + y3 ** 2))) < 0:
    print("Тупокутний")
else:
    print("Інше")
