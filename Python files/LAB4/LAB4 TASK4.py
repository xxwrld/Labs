a = float(input())
b = float(input())
c = float(input())
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
