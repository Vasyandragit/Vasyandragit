class Rectangle:
    def __init__(self, point1, point2):
        self.a = abs(point1[0] - point2[0])
        self.b = abs(point1[1] - point2[1])
    
    def perimeter(self):
        return round(2 * self.a + 2 * self.b, 2) 
    
    def area(self):
        return round(self.a * self.b, 2)