import math

n = int(input("Введіть значення n :"))

a = [math.cos(1)]
for i in range(1, n):
    a.append(((2 * (i + 1) - 1) * math.cos(i + 1) + a[i - 1]) / (((i + 1) ** 2) + a[i - 1]))
h = [el ** 2 for el in a if el > 0]
m = [el ** 2 for el in a if el < 0]
if sum(m) > sum(h):
    print("z=-1")
elif sum(m) < sum(h):
    print("z=1")
