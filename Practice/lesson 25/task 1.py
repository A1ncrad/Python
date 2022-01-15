class Circle:
    P = 3.14
    c_v = 0
    def __init__(self, r):
        self.r = r
        Circle.c_v += 1
    def length(self):
        l = 2 * self.P * self.r
        print(f"Длинна окружности = {l}")
    def square(self):
        s = self.P * self.r ** 2
        print(f"Площадь окружности = {s}")

while True:
    radius = int(input(f"Введите радиус круга, чтобы вычислить формулы\nВведите `0`, чтобы завершить задание: "))
    if radius == 0:
        print("Цикл завершен!")
        break
    else:
        if radius < 0:
            print("Цикл не может быть равен, меньше 0!")
            break
        else:
            crl = Circle(radius)
            crl.length()
            crl.square()
            print(f"Количество кругов: {Circle.c_v}")
