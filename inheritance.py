class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):  # Dog class inherits from Animal class
    def __init__(self, breed):
        super().__init__("Dog")
        self.breed = breed

    def make_sound(self):
        print("Woof!")

class Cat(Animal):  # Cat class inherits from Animal class
    def __init__(self, breed):
        super().__init__("Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!")

# Create instances of Dog and Cat
dog = Dog("Labrador")
cat = Cat("Persian")

# Call methods of parent class and subclass
print(dog.species)  # Output: Dog
dog.make_sound()    # Output: Woof!

print(cat.species)  # Output: Cat
cat.make_sound()    # Output: Meow!

tiger = Animal("Tiger")
print(tiger.species)  # Output: Tiger
tiger.make_sound()    # Output: Some generic animal sound
