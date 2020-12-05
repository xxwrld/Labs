def recursion(i):
    if i == 0 or i == 1:
        return 1
    else:
        return (recursion(i-1)) + (2*recursion(i-2))
    pass


n = int(input('n = '))
print('х{0} = {1}'.format(n, recursion(n)))
