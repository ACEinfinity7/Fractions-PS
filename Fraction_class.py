class Fraction():

    num = None
    den = None

    def __init__(self, num, den):
        #makes num and den 'nice' and adds them as members
        num, den = self.fix_fraction(num,den)
        self.num = num
        self.den = den

    def __str__(self):
        #prints stored fraction with proper formatting
        return f'fraction is {self.make_mixed(self.num, self.den)}'

    def make_mixed(self, a, b):
        #makes mixed by taking den out of num until num is less than den
        whole = 0
        while a >= b:
            a -= b
            whole += 1

        if whole > 0:
            if a == 0:
                #returns whole number if completly factors out
                return f'{whole}'
            return f'{whole} {a}/{b}'
        return f'{a}/{b}'


    def gcd(self,a, b):
        #uses gcd from earlier in problem set
        #finds gcd by taking a out of b
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

    def fix_fraction(self,a,b):
        #makes a double negative num and den both pos
        #moves negative from den to num
        if b != abs(b) and a != abs(a):
            b = abs(b)
            a = abs(a)
        if b != abs(b) and a == abs(a):
            b = abs(b)
            a = -a
        return a,b

    def __add__(self,a,b):
        #makes dens equal and adds nums
        a,b = self.fix_fraction(a,b)
        num = self.num*b + a*self.den
        den = self.num*b
        div = self.gcd(num,den)
        num //= div
        den //= div
        return self.make_mixed(num,den)

    def __sub__(self,a,b):
        #calls addition with negative num
        return self.__add__(-a,b)

    def __mul__(self,a,b):
        #numtiplies nums and dens and reduces
        a,b= self.fix_fraction(a,b)
        num = self.num * a
        den = self.den * b
        div = self.gcd(num, den)
        num //= div
        den //= div
        return self.make_mixed(num,den)

    def __div__(self,a,b):
        #calls mul with flipped fraction
        return self.__mul__(b,a)

    def __eq__(self,a,b):
        #checks for equality after dens are same
        a,b = self.fix_fraction(a,b)
        if self.num * b == a *self.den:
            return True
        return False

    def __gt__(self,a,b):
        #checks if input is greater than stored after dens are same
        a,b = fix_fraction(a,b)
        return True if a*self.den > self.num*b else False

    def __lt__(self,a,b):
        #checks if input is less than stored after dens are same
        a,b = fix_fraction(a,b)
        return True if a*self.den < self.num*b else False






frac = Fraction(3,2)
print(frac)
print(frac.__add__(1,2))
print(frac.__sub__(1,2))
print(frac.__mul__(1,2))
print(frac.__div__(1,2))
