n = input('Введіть n ')
k = 9
c = 9
for i in n:
    k = int(i)
    if k < c:
        c = k
print("Найменша цифра = " c)
