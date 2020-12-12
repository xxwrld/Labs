import datetime


class Car:
    def __init__(self, _a, _b, _c, _f, _k, _n, _y):
        self.a = _a  # manufacturer(Ford, Dodge...)
        self.b = _b  # about_manufacturer
        self.c = _c  # about_seller
        self.f = _f  # about_owner
        self.k = _k  # color
        self.n = _n  # number
        self.y = _y  # year

    def car_age(self):
        now = datetime.date.today()
        delta = now - self.y
        return delta

    def changes_owner(self, x, y):
        self.f = [x, y]

###tests###
##Owner
# f=Car(0,0,0,0,0,0,0)
# f.changes_owner(5,6)
# print(f.f)
##Car_Age
# f = Car( datetime.date(1997, 6, 23))
# print(f.car_age())
