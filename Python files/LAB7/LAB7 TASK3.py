n = int(input("n="))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
b = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
c = [[[] for el1 in range(n)] for el in range(n)]
for z in range(n):
    for k in range(n):
        d = sum([a[z][l] * b[l][k] for l in range(n)])
        c[z][k] = d
for i in range(n):
    print(c[i])
