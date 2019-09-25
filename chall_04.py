class Bib:
    def __init__(self):
        self.star = "Go"
        self.stop = "Stop"

two = Bib()
one_two = two
print(two is one_two)

three = Bib()
print(two is three)