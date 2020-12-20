import datetime


class manufacturer:
    def __init__(self, _a, _b, _c, _d):
        self.a = _a  # name_manufacturer
        self.b = _b  # foundation_year
        self.c = _c  # phone_number
        self.d = _d  # production_volumes
class seller:
    def __init__(self, _g, _j, _l, _q):
        self.g = _g  # name_manufacturer
        self.j = _j  # foundation_year
        self.l = _l  # phone_number
        self.q = _q  # production_volumes
class owner:
    def __init__(self, _f, _p):
        self.f = _f  # about_owner
        self.p = _p  # owner_id
    def change(self,x,y):
        self.f = x
        self.p = y

class Car:
    def __init__(self, _k, _n, _t, _a, _b, _c, _d, _g, _j, _l, _q, _f, _p, _y):
        self.k = _k  # color
        self.n = _n  # number
        self.t = _t  # name
        self.manufacturer = manufacturer(_a, _b, _c, _d)
        self.seller = seller(_g, _j, _l, _q)
        self.owner = owner( _f, _p)
        self.age = _y

    def changes_owner(self, x, y):
        self.owner.change(x,y)


    def car_age(self):
        now = datetime.date.today()
        delta = now - self.age
        return delta


