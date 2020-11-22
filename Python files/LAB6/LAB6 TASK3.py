import math

n = int(input('Введіть значення n ='))
a = input('Координати вектора а = ').split(' ')
b = input('Координати вектора b = ').split(' ')
a = [float(el) for el in a]
b = [float(el) for el in b]
ab = 0
for i in range(n):
    ab += float(a[i]) * float(b[i])
a_square = [el ** 2 for el in a]
b_square = [el ** 2 for el in b]
cos_a_b = ab / (math.sqrt(sum(a_square)) * math.sqrt(sum(b_square)))
sin_a_b = math.sqrt(1 - cos_a_b ** 2)
s = sin_a_b * math.sqrt(sum(a_square)) * math.sqrt(sum(b_square))
print('Векторний добуток векторів =', s)
