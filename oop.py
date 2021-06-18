#Importing and Inheriting
#Encapsulation
#Getters - just returning a value so no need to pass parameters
#Setters - changing or adding a value so have to pass parameters

'''
INHERITING --
eg.
from animal import animal
class bird(animal):     <- how to inherit
'''

from animal import animal
class bird(animal):
    pass

newBird = bird("owl", "carnivore")
print(newBird.getName())


'''
IMPORTING w/out inheriting
'''
from animal import animal
class bird:
    newAnimal = animal("owl", "carnivore")
    def printName(self):
        print(self.newAnimal.getName())

newBird = bird()
newBird.printName()


'''
importing no inheriting 2
'''
from animal import animal
class bird:
    newAnimal = animal("owl", "carnivore")

newBird = bird()

print(newBird.newAnimal.getName())

'''
ENCAPSULATION
 - When you want to restrict access of a property from one class (eg. parent class) to another (eg. children class).
 - As in you make a property in the parent class unable to be modified by the child class.
 - Access modifiers
1. public - no underscore
2. protected - single underscore _
3. private - double underscore __
'''

