class Rectangle:
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1[0], point1[1]
        self.x2, self.y2 = point2[0], point2[1]
        
        self.a = abs(self.x1 - self.x2)
        self.b = abs(self.y1 - self.y2)
        
    def get_pos(self):
        return (round(min(self.x1, self.x2), 2), round(max(self.y1, self.y2), 2))
    
    def get_size(self):
        return (round(self.a, 2), round(self.b, 2))
    
    def move(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
    
    def resize(self, width, height):
        self.a, self.b = width, height
         
    def perimeter(self):
        return round(2 * self.a + 2 * self.b, 2) 
    
    def area(self):
        return round(self.a * self.b, 2)

