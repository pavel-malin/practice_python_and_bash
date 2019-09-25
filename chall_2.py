import math

class Circle:
    def __init__(self, r, n):
        self.radius = r
        self.number = n

    def area(self):
        return self.number/math.pi * self.radius

circle = Circle(10, 2)
print(circle.area())