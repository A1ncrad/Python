side = int(input("Введите сторону квадрата: "))
r = int(input("Введите радиус вписанного круга: "))
if r == side / 2:
    print("Круг можно вписать!")
else:
    print("Круг вписать нельзя!")
