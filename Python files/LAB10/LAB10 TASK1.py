class Number:
    def __init__(self, _a):
        self.a = _a

    def change(self, _a):
        self.a = _a

    def return_number(self):
        return self.a

    def count_digit_in_number(self):
        return len(list(self.a))

    def sum_digit_in_number(self):
        return sum(list(map(float, list(self.a)))