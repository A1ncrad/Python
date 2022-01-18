class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def square(self):
        s = self.length * self.width
        print(f"Площадь прямоугольника равна: {s}")


l = int(input("Введите длину стороны прямоугольника: "))
w = int(input("Введите ширину стороны прямоугольника: "))

rectangle_1 = Rectangle(l, w)

rectangle_1.square()
