n = int(input('Введіть n '))
x0 = 0
x1 = 9
i = 1
if n == 1:
    total = x1
else:
    while i < n:
        i += 1
        x2 = 2 * x1 + 3 * x0
        x0 = x1
        x1 = x2
    total = x2
print('x{0} = {1}'.format(n, total))
## x(n) = result
