class Human:
    def __init__(self, name, surname, place_of_birth, age, year):              
        self.name = name
        self.surname = surname
        self.place_of_birth = place_of_birth
        self.age = age
        self.year = year


    def info(self):
        print(f"Human:\n\tИмя: {self.name}\n\tФамилия: {self.surname}\n\tМесто рождение: {self.place_of_birth}\n\tВозраст: {self.age}\n\tГод рождения:{self.year}")

p1 = Human("Den", "Dmitriev", "UA", 24, 1997)

p2 = Human("Renat", "Bershadskiy", "UA", 14, 2007)

p1.info()
p2.info()
