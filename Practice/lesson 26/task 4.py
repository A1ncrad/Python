import math

x = int(input("Введите х: "))
y = int(input("Введите у: "))

if 1 > abs(x * y) and x < 0:
      z = (x + y) /(math.e ** x * y)
      print(z)
elif y <= 0 and x > 2:
    z =- (math.log(x)) ** 2
    print(z)
elif y > 0 and x >= 0 and x <= 2:
    z = math.log(math.sqrt(y))
    print(z)
else:
    print("Error")
