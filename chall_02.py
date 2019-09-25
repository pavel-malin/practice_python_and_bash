class Horse():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider():
    def __init__(self, name):
        self.name = name

poristar = Rider("Moris Hasle")
ofi = Horse("Ofi", "Mustang", poristar)
print(ofi.owner.poristar)