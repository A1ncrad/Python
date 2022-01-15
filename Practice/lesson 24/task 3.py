class Human:
    def count_age(self, m):
        return m - self.year


year = int(input("Введите год, на сегодняшний момент: "))
p1 = Human()
p1.name = "Timur"
p1.surname = "Bratcev"
p1.place_of_birth = "UA"
p1.year = 2007

p2 = Human()
p2.name = "Yarick"
p2.surname ="Bershatskiy"
p2.place_of_birth = "UA"
p2.year = 2006

print(f"Возраст первого человека: {p1.count_age(year)}")
print(f"Возраст второго человека: {p2.count_age(year)}")
