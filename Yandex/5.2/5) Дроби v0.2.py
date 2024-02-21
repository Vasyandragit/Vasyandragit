def nod(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            a, b = [int(i) for i in args[0].split('/')]
        elif len(args) == 2:
            a, b = args[0], args[1]
        
        sokr = nod(a, b)
        a //= sokr
        b //= sokr
        self.a, self.b = a, b
        
    def numerator(self, number=0):
        if number:
            self.a = number
            sokr = nod(self.a, self.b)
            self.a //= sokr
            self.b //= sokr
        else:
            return abs(self.a)
        
    def denominator(self, number=0):
        if number:
            self.b = abs(number)
            self.a = self.a * -1 if number < 0 else self.a
            sokr = nod(self.a, self.b)
            self.a //= sokr
            self.b //= sokr
        else:
            return abs(self.b)
    
    def __str__(self):
        return f"{self.a}/{self.b}"
    
    def __repr__(self):
        return f"Fraction('{self.a}/{self.b}')"
    
    def __neg__(self):
        return Fraction(-self.a, self.b)

a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())