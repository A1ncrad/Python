import math


a = int(input("Введите сторону равностороннего треугольника: "))
r = int(input("Введите радиус круга: "))
if r == a * math.sqrt(3) / 6:
    print("Можно вписать круг")
else:
    print("Вписать нельзя")
