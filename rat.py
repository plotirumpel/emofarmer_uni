import math

class Rational:

    def __init__(self, numerator, denominator=1):
        self._n = numerator
        self._d = denominator
        nod = math.gcd(self._n, self._d)
        self._n, self._d = self._n // nod, self._d // nod
        if self._d < 0:
            self._n, self._d = -self._n, -self._d

    def __str__(self):
        strans = f'{self._n}'+'/'+f'{self._d}'
        strans = strans.replace('/1', '')
        strans = strans.replace('0/', '')
        return strans

    def as_number (self):
        return self._n/self._d

    def reduction (self):
        nod = math.gcd(self._n, self._d)
        self._n, self._d = self._n//nod, self._d//nod
        if self._d < 0:
            self._n, self._d = -self._n, -self._d
        return self

    def __add__(self, a):
        if (self._d == a._d):
            num = self._n + a._n
            den = self._d
        else:
            den = math.lcm(self._d, a._d)
            num = self._n*(den//self._d) + a._n*(den//a._d)
        return Rational(num, den)

    def __iadd__(self, a):
        if (self._d == a._d):
            self._n += a._n
        else:
            lcm = math.lcm(self._d, a._d)
            self._n = self._n * (lcm // self._d) + a._n * (lcm//a._d)
            self._d = lcm
        return self.reduction()

    def __sub__(self, s):
        if (self._d == s._d):
            num = self._n - s._n
            den = self._d
        else:
            den = math.lcm(self._d, s._d)
            num = self._n * (den // self._d) - s._n * (den // s._d)
        return Rational(num, den)

    def __isub__(self, s):
        if (self._d == s._d):
            self._n -= s._n
        else:
            lcm = math.lcm(self._d, s._d)
            self._n = self._n * (lcm // self._d) - s._n * (lcm // s._d)
            self._d = lcm
        return self.reduction()

    def __mul__(self, m):
        num = self._n * m._n
        den = self._d * m._d
        return Rational(num, den)

    def __imul__(self, m):
        self._n = self._n * m._n
        self._d = self._d * m._d
        return self.reduction()

    def __truediv__(self, d):
        num = self._n * d._d
        den = self._d * d._n
        return Rational(num, den)

    def __itruediv__(self, d):
        self._n = self._n * d._d
        self._d = self._d * d._n
        return self.reduction()

    def __eq__(self, other):
        return self._n == other._n and self._d == other._d

    def __nq__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if (self._n == other._n):
            return self._d < other._d
        elif (self._d == other._d):
            return self._n > self._d
        else:
            lcm = math.lcm(self._d, other._d)
            self._n, other._n = self._n * (lcm // self._d), other._n * (lcm // other._d)
            return self._n > other._n

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        return not self.__gt__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)


