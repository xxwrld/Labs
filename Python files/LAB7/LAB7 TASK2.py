n = int(input('n='))
j = int(input('column='))
i = int(input('line='))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
s = 0
for z in range(n):
    s += a[i][z] * a[z][j]
print(s)
