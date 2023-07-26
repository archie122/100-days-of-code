class Animal:
    def __init__(self):
        self.name = "cat"
        self.age = 12

    def breathe(self):
        print("Breath in, Breath out.")

class Fish(Animal):
    def __init__(self):
        super().__init__() #This is the proper way of getting the functionality from one function to another
    def swim(self):
        print("Swimming")

    def breathe(self):
        super().breathe() #This is the way to building on top to the already existing class
        print("Underwater breathing")


nemo = Fish()
nemo.breathe()
nemo.swim()