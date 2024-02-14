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
            