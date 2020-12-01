n = int(input('n='))
a = [[float(input('a[{0}][{1}]='.format(i, j))) for j in range(n)] for i in range(n)]
b = []
for j in range(1, n+1):
    z = []
    for k in range(j):
        z.append(a[n-k-1][n-(n+k-j)-1])
    b.append(z)
    z = []
    for k in range(j):
        z.append(a[k][n + k - j])
    b.append(z)
d = [a[i][i] for i in range(n)]
b.remove(d)
d.reverse()
b.remove(d)
for i1 in range(len(b)):
    b[i1] = sum(b[i1])
print(max(b))
