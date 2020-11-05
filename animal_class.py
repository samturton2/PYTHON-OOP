# Creating an Animal class as PARENT/BASE/SUPER class

class Animal:

    def __init__(self): # initialising animal class
        self.alive = True # creating an attribute/ variable
        self.spine = True
        self.eyes = True
        self.lungs = True

    # create behaviours
    def breathe(self):
        return "keep breathing to stay alive"

    def move(self):
        return "left to right and up and down"

    def eat(self):
        return "nom nom nom"

    def procreate(self):
        return "find partner"

# # instantiate our class/ create an object
# cat = Animal() # creating an object of Animal class
# # cat as child inherits everything everything from Animal/ parent class
# print(cat.eat())