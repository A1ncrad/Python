class Human:
    def __init__(self, name,  surname, year_of_birth, place_of_birth):
        self.name = name
        self.surname = surname
        self.year_of_birth = year_of_birth
        self.place_of_birth = place_of_birth

    def info(self):
        print(f"Name: {self.name} \nSurname: {self.surname} \nYear of birth: {self.year_of_birth} \nPlace of birth: {self.place_of_birth}")

    def age(self, years):
        return years - self.year_of_birth

name = input("Введите своё имя: ")
surname = input("Введите свою фамилию: ")
year_of_birth = int(input("Введите год рождения: "))
place_of_birth = input("Введите место рождения: ")
years = int(input("Введите текущий год: "))
p1 = Human(name, surname, year_of_birth, place_of_birth)
p1.info()
print(p1.age(years))

name2 = input("Введите своё имя: ")
surname2 = input("Введите свою фамилию: ")
year_of_birth2 = int(input("Введите год рождения: "))
place_of_birth2 = input("Введите место рождения: ")
years2 = int(input("Введите текущий год: "))
p2 = Human(name2, surname2, year_of_birth2, place_of_birth2)
p2.info()
print(p2.age(years2))
