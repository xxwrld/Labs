a = input('Координати вектора а = ').split(' ')
b = input('Координати вектора b = ').split(' ')
a = [float(el) for el in a]
b = [float(el) for el in b]
c=[]
ax = a[0]
ay = a[1]
az = a[2]
bx = b[0]
by = b[1]
bz = b[2]
c.append(ay*bz-az*by)
c.append(az*bx - ax*bz)
c.append(ax*by - ay*bx)
print(c)