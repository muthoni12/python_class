class animal:
    _colour = "brown"
    def __init__(self, name, foodtype):
        self.name = name
        self.foodtype = foodtype

    def getName(self):
        return self.name

    def getfoodType(self):
        return self.foodtype

    def setName(self, name):
        self.name = name

    def setfoodType(self, foodtype):
        self.foodtype = foodtype
    
    def getColour(self):
        return self._colour

    def setColour(self, colour):
        self._colour = colour

    def run(self, origin, destination):
        #logic
        pass

newAnimal = animal("fox", "omnivore")

newAnimal.run("-133.49, 00.10", "-0.24, 1.0")

print(newAnimal.getfoodType())
print(newAnimal.getColour())
print(newAnimal.getName())