class Human:
    def info(self,n):
        for i in range(n):
            print(f"\tHuman_1:\nИмя: {self.name}\nФамилия: {self.surname}\nМесто рождение: {self.place_of_birth}")

n = int(input("Введите количество выводов для первого человека: "))
m = int(input("Введите количество выводов для второго человека: "))
p1 = Human()
p1.name = "Timur"
p1.surname = "Bratcev"
p1.place_of_birth = "UA"

p2 = Human()
p2.name = "Renat"
p2.surname = "Bershatskiy"
p2.place_of_birth = "UA"

p1.info(n)
p2.info(m)
#print(f'Human_1:\nИмя: {p1.name}\nФамилия: {p1.surname}\nМесто рождение: {p1.place_of_birth} ')
#print(f'Human_2:\nИмя: {p2.name}\nФамилия: {p2.surname}\nМесто рождение: {p2.place_of_birth} ')
