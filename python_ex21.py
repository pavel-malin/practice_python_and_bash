class Lion:
    def __init__(self, name):
        self.name = name

# lion = Lion("Дилберт")
# print(lion)
# >> <__main__.Lion object at 0x101178828>
    
    def __repr__(self):
        return self.name

lion = Lion("Дилберт")
print(lion)