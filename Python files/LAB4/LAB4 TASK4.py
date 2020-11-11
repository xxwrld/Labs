a = float(input("Введіть значення a :"))
b = float(input("Введіть значення b :"))
c = float(input("Введіть значення c :"))
if a < b < c:
    print("1")
elif a == b == c:
    print("2")
elif b < a < c:
    print("3")
elif c < a < b:
    print("4")
else:
    print("0")
