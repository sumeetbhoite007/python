class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.x}, {self.y}"
    
    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y
    
    def draw(self):
        print (f"values: {self.x} and {self.y}")
        
        
point = Point(1, 2)
other = Point(0, 1)
print(point >= other)