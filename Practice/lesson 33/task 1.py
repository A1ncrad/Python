class Animal:
    def __init__(self, species):
        self.species = species
        self.sound = "Grr!"
    def show_species(self):
        print(f"Species of animal : {self.species}")

    def animal_sound(self):
        print(f"{self.sound}")


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.sound = "Meow!"

        
class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.sound = "Woof! Woof!"

def show_animal_info(animal):
    try:
        animal.show_species()
        animal.animal_sound()
    except AttributeError:
        print(f"{animal} is not animal!")

an = Animal("monkey")
cat = Cat("cat")
dog = Dog("dog")

show_animal_info(an)
show_animal_info(cat)
show_animal_info(dog)
show_animal_info("Book")
