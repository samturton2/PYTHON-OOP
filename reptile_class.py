# creating a reptile class as a child class of our Animal class
from animal_class import Animal
# syntax to import files and classes

class Reptile(Animal):
    def __init__(self):
        # super key word is used to inherit everything from parent class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    # creating function for our reptile class
    def seek_heat(self):
        return "i need heat"

    def hunt(self):
        return "get me some scran"

# # Let's create an object of our reptile class to utilise the amazing functionalities of OOP
# reptile_object = Reptile()
#
# print(reptile_object.eat())
# print(reptile_object.breathe())
# print(reptile_object.procreate())
# print("the above functionalities are inherited from our Animal/ Parent class")
#
# print(reptile_object.hunt())