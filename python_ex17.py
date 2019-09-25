class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l
    
    def print_size(self):
        print("""{} by {}
             """.format(self.width, self.len))

# my_shape = Shape(20, 20)
# my_shape.print_size()
# >> 20 by 20

class Square(Shape):
#    pass
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("""I {} by {}
              """.format(self.width, self.len))

a_square = Square(20, 20)
# a_square.print_size()
# >> 20 by 20
# print(a_square.area())
# >> 400
# a_square.print_size()
# >> I 20 by 20