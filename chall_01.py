class Square():

    def __init__(self, l, u):
        self.len = l
        self.ugal = u

    def calculate_perimeter(self):
        return self.len * self.ugal

    def change_size(self):
        if square.calculate_perimeter() >= 40:
            self.len -= 1
            self.ugal -= 1
        if square.calculate_perimeter() <= 40:
            self.len += 1
            self.len += 1

   # def calculate_perimeter(self):
   #     return self.len * self.ugal

class Rectangle(Square):

    def __init__(self, l, u):
        self.len = l
        self.ugal = u


class Shape(Square):

    def what_am_i(self):
        print("I am a figure.")

square = Square(20, 2)
square.calculate_perimeter()

rectangle = Rectangle(10, 2)
rectangle.change_size()
print(rectangle.calculate_perimeter())



shape = Shape(20, 2)
shape.change_size()
print(shape.calculate_perimeter())
shape.what_am_i()