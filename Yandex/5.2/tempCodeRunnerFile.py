def nod(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            a, b = int(args[0][:args[0].find('/')]), int(args[0][args[0].find('/') + 1:])
        elif len(args) == 2:
            a, b = args[0], args[1]
        
        sokr = nod(a, b)
        a //= sokr
        b //= sokr
        self.a, self.b = a, b
        
    
    def numerator(self, number=0):
        if number:
            self.a += number
            sokr = nod(self.a, self.b)
            self.a //= sokr
            self.b //= sokr
        else:
            return self.a
        
    def denominator(self, number=0):
        if number:
            self.b += number
            sokr = nod(self.a, self.b)
            self.a //= sokr
            self.b //= sokr
        else:
            return self.b
    
    def __str__(self):
        return f"{self.a}/{self.b}"
    
    def __repr__(self):
        return f"Fraction({self.a, self.b})"
    