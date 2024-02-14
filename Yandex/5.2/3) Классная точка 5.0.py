class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point2):
        x2, y2 = point2.x, point2.y
        return round(((self.x - x2) ** 2 + (self.y - y2) ** 2) ** 0.5, 2) 


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            self.x = self.y = 0
            
        elif len(args) == 1:
            self.x, self.y = args[0]
            
        elif len(args) == 2:
            self.x, self.y = args[0], args[1]
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
    
    def __add__(self, other):
        new_point = PatchedPoint(self.x + other[0], self.y + other[1])
        return new_point
    
    def __iadd__(self, other):
        self.move(other[0], other[1])
        return self
        
first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)