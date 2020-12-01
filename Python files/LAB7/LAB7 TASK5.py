n = int(input('n='))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
b = []
for i in range(n):
    if len([el for el in a[i] if el >= 0]) == n:
        b.extend(a[i])
d = 1
for i in range(len(b)):
    d *= b[i]
print(d)
