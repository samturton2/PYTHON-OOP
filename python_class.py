# Creating a python class as child class of our snake class

from snake_class import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.venom = True
        self.two_lungs = True

    # creating functions for our python class
    def digest_large_prey(self):
        return "yum yum yum"

    def climb(self):
        return "im gonna be high up"

    def shed_skin(self):
        return "look at my new skin!"

if __name__ == "__main__":
    python_object = Python()

    print(python_object.breathe()) # function from animal class
    print(python_object.hunt()) # function from reptile class
    print(python_object.use_venom()) # function from snake class
    print(python_object.shed_skin()) # function from python class