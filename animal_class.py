# Creating an Animal class as PARENT/BASE/SUPER class

class Animal:

    def __init__(self): # initialising animal class
        self.alive = True # creating an attribute/ variable
        self.spine = True
        self.eyes = True
        self.lungs = True

    # create behaviours
    def breathe(self):
        if self.alive == True:
            return "keep breathing to stay alive"
        else:
            return "You are dead"

    def move(self):
        if self.alive == True:
            return "left to right and up and down"
        else:
            return "You are dead"

    def eat(self):
        if self.alive == True:
            return "nom nom nom"
        else:
            return "You are dead"

    def procreate(self):
        if self.alive == True:
            return "find partner"
        else:
            return "You are dead"

# # instantiate our class/ create an object
# cat = Animal() # creating an object of Animal class
# # cat as child inherits everything everything from Animal/ parent class
# print(cat.eat())