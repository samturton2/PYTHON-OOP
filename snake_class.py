# creating a snake class as child of reptile class
from reptile_class import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__() # include all attributes of parent class
        self.forked_tongue = True
        self.venom = bool
        self.limbs = False


    def use_venom(self):
        if self.venom == True:
            return "POISON"
        else:
            return "You have no poison"

    def use_tongue_to_smell(self):
        return "lick lick hiss"

