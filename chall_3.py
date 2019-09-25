class Triangle:

    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        square = 1/2 * self.width*self.len
        self.square = square
        print(self.square)

triangle = Triangle(10, 3)
print(triangle.area())