n = int(input('n='))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
b = []
for i in range(n):
    if len([el for el in a[i] if el >= 0]) == n:
        b.append(a[i])
for j in range(len(b)):
    d = 1
    for i in range(len(b[j])):
        d *= b[j][i]
    b[j]=d
print(b)
