class Square():
    square_list = []

    def __init__(self, number, width, l, big):
        self.number = number
        self.width = width
        self.len = l
        self.big = big
        self.square_list.append((self.number))

    def print_list(self):
        print("""{} by {} by {} by {}""".format(self.number, self.len,
                                                self.width, self.big))

s1 = Square(20, 20, 20, 20)
s2 = Square(10, 10, 10, 10)
s3 = Square(40, 40, 40, 40)
s4 = Square(20, 20, 20, 20)

print(Square.square_list)
print(s1.print_list(), s2.print_list(), s3.print_list(), s4.print_list())