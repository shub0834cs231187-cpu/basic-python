# 2. Rectangle Class — Calculate Area

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r = Rectangle(5, 3)
r1 = Rectangle(7,5)
r2= Rectangle(8,4)
print("Area:", r.area(),r1.area(),r2.area())
