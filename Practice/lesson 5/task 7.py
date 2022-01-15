x =int(input("Введите значение x: "))
a =int(input("Введите значение a: "))
if x > 0:
    if a >= 0:
        y = a * x
        print(y)
    else:
        y = 2 * a * x
        print(y)
else:
    y = 2
    print(y)
