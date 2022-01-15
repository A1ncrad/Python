class Pet:
    def __init__(self, animal, name, age, kind_of_animal):
        self.animal = animal
        self.name = name
        self.age = age
        self.kind_of_animal = kind_of_animal

    def info(self):
        print(f"Animal:{self.animal}\nName of pet: {self.name}\nAge: {self.age}\nKind of animal: {self.kind_of_animal}")

    def history(self):
        h = f"""
            When I was 10 years old, I wanted to have a rabbit. For my 11th birthday my parents gifted me a little
            {self.animal} breed {self.kind_of_animal}, I was very surprised. I called him {self.name}. He is now 
            {self.age} years old.
            """
        print(h)


my_pet = Pet("Rabbit", "White",  3, "Hermelin")

my_pet.info()
my_pet.history()
