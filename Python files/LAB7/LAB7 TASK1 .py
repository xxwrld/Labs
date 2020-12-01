n = int(input("n="))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
b = []
for i in range(n):
    b.extend(a[i][i + 1:])
b = [el for el in b if el > 0]
d = 1
for i in range(len(b)):
    d *= b[i]
print(d)
