import math


class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = (result.denominator // self.denominator) * self.numerator + \
                           (result.denominator // other.denominator) * other.numerator
        result.simplify()
        return result

    def __sub__(self, other):
        result = Fraction()
        result.denominator = math.lcm(self.denominator, other.denominator)
        result.numerator = (result.denominator // self.denominator) * self.numerator - \
                           (result.denominator // other.denominator) * other.numerator
        result.simplify()
        return result

    def simplify(self):
        g = math.gcd(self.denominator, self.numerator)
        self.denominator //= g
        self.numerator //= g

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


p1 = Fraction(1, 5)
p2 = Fraction(2, 5)
p3 = Fraction(2, 8)
p4 = Fraction(2, 9)
fsum = p1 + p2 + p3 + p4
fdif = p1 + p2 - p3 - p4
print(f'{p1} + {p2} + {p3} + {p4} = {fsum}')
print(f'{p1} + {p2} - {p3} - {p4} = {fdif}')
