from animal import animal

class bird(animal):
    def fly():
        #logic
        pass

newBird = bird("owl", "carnivore")
newBird.setColour("white")
print(newBird.getColour())
print(newBird.getName())
