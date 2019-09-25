class Hexagon:

    def __init__(self, l, u='6'):
        self.ugal = u
        self.len = l

    def calculate_perimeter(self):
        r = (self.len * (3 ** 2)) / 2
        self.radius = r
        s = ((3 * (3 ** 2)) / 2) * (self.len ** 2)
        self.square = s
        p = self.ugal * self.len
        self.perimeter = p
        print("Perimeter: " + str(self.perimeter) + "; Radius: " + 
              str(self.radius) + "; Square: " + str(self.square))

hexagon = Hexagon(2)
print(hexagon.calculate_perimeter())
