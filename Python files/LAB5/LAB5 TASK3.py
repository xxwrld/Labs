from math import factorial
from math import log

a = float(input("Введіть значення a :"))
x = float(input("Введіть значення x :"))
epsilon = float(input("Заданна точність:"))
degree_a = a ** x
s = 0
fraction1 = 1
i = 0
while fraction1 > epsilon:
    i += 1
    fraction2 = fraction1
    s += fraction2
    fraction1 = ((x * log(a)) ** i) / factorial(i)
if degree_a == s:
    print('Справедливість вірна')
else:
    print('Справедливість невірна')