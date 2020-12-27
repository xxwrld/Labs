class TTriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def input_a(self, a):
        self.a = a

    def input_b(self, b):
        self.b = b

    def input_c(self, b):
        self.b = b

    def print_a(self):
        return self.a

    def print_b(self):
        return self.b

    def print_c(self):
        return self.c

    def square(self):
        side_a = ((self.perimeter() / 2) - self.a)
        side_b = ((self.perimeter() / 2) - self.b)
        side_c = ((self.perimeter() / 2) - self.c)
        return ((self.perimeter() / 2) * side_a * side_b * side_c) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def __lt__(self, other_triangle):
        if t1 < t2:
            print('First triangle is considered as lower then second')
            return self.square() < other_triangle.s()


#####
t1 = TTriangle(2, 4, 3)
print(t1.print_a())
print(t1.print_b())
print(t1.print_c())
s = t1.square()
print(s)
t2 = TTriangle(2, 5, 7)
print(t2.print_a())
print(t2.print_b())
print(t2.print_c())
print(t2.square())
