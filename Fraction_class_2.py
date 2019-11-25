class Fraction():
    num = None
    den = None

    def __init__(self,num,den):
        if den == 0:
            raise ValueError("Denominator must not be zero.")
        self.num = num
        self.den = den
        self.fix()
        self.simplify()

    def fix(self):
        if self.den <= 0 and self.num <= 0:
            self.num = abs(self.num)
            self.den = abs(self.den)
        if self.den <= 0 and self.num >= 0:
            self.num = -self.num
            self.den = -self.den

    def simplify(self):
        div = self.gcd(self.num,self.den)
        self.num //= div
        self.den //= div

    @staticmethod
    def gcd(a,b):
        a,b = abs(a),abs(b)
        if a == 0 and b == 0:
            return a
        if a == 0:
            return b
        if b == 0:
            return a
        while a != b:
            if b < a:
                a,b = b,a
            b -= a
        return a

    @staticmethod
    def make_mixed(a,b):
        mixed_frac_whole = '%d' % (a // b)
        mixed_frac_frac = '%d/%d' % (a % b, b)
        if mixed_frac_whole == '0':
            return mixed_frac_frac
        if mixed_frac_frac[0] == '0':
            return mixed_frac_whole
        return f'{mixed_frac_whole} {mixed_frac_frac}'

        return

    @staticmethod
    def invert(other):
        return Fraction(other.den, other.num)

    @staticmethod
    def int_to_obj(val):
        if not isinstance(val, Fraction):
            return Fraction(val, 1)
        return val


    def __str__(self):
        return f'fraction is {self.make_mixed(self.num,self.den)}'

    def __add__(self,other):
        other = self.int_to_obj(other)
        if isinstance(other, int):
            other = Fraction(other, 1)
        num = self.num*other.den + other.num*self.den
        den = self.den*other.den
        return Fraction(num,den)

    def __radd__(self, other):
        return Fraction(other,1) + self

    def __sub__(self,other):
        other = self.int_to_obj(other)
        return self + Fraction(-other.num, other.den)

    def __rsub__(self,other):
        return Fraction(other,1) - self

    def __mul__(self,other):
        other = self.int_to_obj(other)
        return Fraction(self.num*other.num,self.den*other.den)

    def __rmul_(self,other):
        return Fraction(other,1) * self

    def __truediv__(self,other):
        other = self.int_to_obj(other)
        return self * self.invert(other)

    def __rtruediv__(self,other):
        return Fraction(other, 1) / self

    def __eq__(self,other):
        other = self.int_to_obj(other)
        return True if self.num*self.den == other.num * self.den else False

    def __gt__(self,other):
        other = self.int_to_obj(other)
        return True if self.num*self.den > other.num * self.den else False

    def __lt__(self,other):
        other = self.int_to_obj(other)
        return True if self.num*self.den < other.num * self.den else False


# frac = Fraction(3,2)
# frac_2 = Fraction(1,2)
# print(frac)
# print(frac_2)
# print(frac + frac_2)
# print(frac - frac_2)
# print(frac * frac_2)
# print(frac / frac_2)
# print(frac == frac_2)
# print(frac > frac_2)
# print(frac < frac_2)
