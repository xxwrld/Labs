n = int(input('n='))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
for j in range(n):
    if j % 2 == 1:
        b = []
        for i in range(n):
            b.append(a[i][j])
        b.sort()
        for i in range(n):
            a[i][j] = b[i]
for i in range(n):
    print(a[i])
