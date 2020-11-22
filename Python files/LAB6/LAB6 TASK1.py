n = int(input('Введіть значення n :'))
a = input().split(' ')
a = [float(el) for el in a]
b = a[0]
for i in range(n):
    if b > a[i]:
        b = a[i]
print('Найменше з числ :', b)
