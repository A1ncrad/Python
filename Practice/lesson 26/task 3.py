import math


x = int(input("Введите х: "))
if x > (-math.pi) and x < math.pi / 4:
    y = math.cos(x - math.pi) ** 2
elif x >= math.pi / 4 and x <= 1:
    y = math.sqrt(abs(x + 1))
elif x > 1:
    y = 1 / (x - 1)
else:
    print("Error")
print(y)
