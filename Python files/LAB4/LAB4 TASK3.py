from math import sqrt

x1 = float(input())
x2 = float(input())
x3 = float(input())
y1 = float(input())
y2 = float(input())
y3 = float(input())
if (-1) < (x1 + x2 + y1 + y2) / (sqrt((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2))) < 0:
    print("Тупокутний")
elif (-1) < (x2 + x3 + y2 + y3) / (sqrt((x2 ** 2 + y2 ** 2) * (x3 ** 2 + y3 ** 2))) < 0:
    print("Тупокутний")
elif (-1) < (x1 + x3 + y1 + y3) / (sqrt((x1 ** 2 + y1 ** 2) * (x3 ** 2 + y3 ** 2))) < 0:
    print("Тупокутний")
else:
    print("Інше")
