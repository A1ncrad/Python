import math


x = int(input('Сторона: '))
r = int(input('Радиус: '))
a = (r * math.sqrt(3)) / 6
if a == x :
    print("Yes!")
else:
    print("No!")
