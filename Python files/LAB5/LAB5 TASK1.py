a = float(input("Введіть значення a :"))
x = float(input("Введіть значення x :"))
n = float(input("Введіть значення n :"))
i = 1
k = (x + a) ** 2
while i < n:
    i += 1
    k = (k + a) ** 2
print("Сума = "k)
