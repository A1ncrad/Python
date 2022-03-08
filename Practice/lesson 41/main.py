import math


# 1


# def greet_user(name):
#     print(f"Hello {name}")


# greet_user("Timur")

# 2


# def copy(line, n):
#     print(line * n)


# copy("Hello", 10)

# 3


# def max_number(a, b):
#     if a > b:
#         print(f"{a} > {b}")
#     elif a < b:
#         print(f"{a} < {b}")
#     else:
#         print("equal")


# max_number(10, 11)

# 4


# def max_of_three(a, b, c):
#     x = max(a, b)
#     y = max(x, c)
#     print(y)


# max_of_three(10, 11, 12)

# 5


# def triangle_true(a, b, c):
#     if a < b + c and b < a + c and c < a + b:
#         print("Существует")
#     else:
#         print("Не существует")


# triangle_true(10, 15, 20)


# 6

# def connect_word(first, second):
#     a = [first, second]
#     print(" ".join(a))


# connect_word("Hello", "World!")

# 7


# def calculator(operand, n, operator):
#     if operator == "+":
#         print("{0:.2f}".format(operand + n))
#     elif operator == "-":
#         print("{0:.2f}".format(operand - n))
#     elif operator == "/":
#         print("{0:.2f}".format(operand / n))
#     elif operator == "*":
#         print("{0:.2f}".format(operand * n))
#     else:
#         print("Unkown operator")


# calculator(2, 7, "/")

# 8


# def tags(tag, string):
#     tag = f"<{tag}>"
#     result = tag + string + tag
#     print(result)


# tag = input("type tag")
# string = input("type content")
# tags(tag, string)

# 9

# year_time = {
#     "winter": (12, 1, 2),
#     "spring": (3, 4, 5),
#     "summer": (6, 7, 8),
#     "autumn": (9, 10, 11)
# }
#
#
# def time_of_year(n):
#     for key, value in year_time.items():
#         if n in value:
#             print(key)


# month = int(input("Input number of month"))
# time_of_year(month)

# 10


# def gistogram(nums):
#     for i in nums:
#         print("*" * i)


# n = [1, 2, 5, 6, 7, 10, 20]
# gistogram(n)

# 11


# def pair_number(n):
#     if n % 2 == 0:
#         print("Парное")
#     else:
#         print("Непарное")


# num = int(input("Number: "))
# pair_number(num)


# 12


# def first_and_lust(*l):
#     result = [l[0], l[-1]]
#     print(result)


# first_and_lust(1, 2, 5, 6, 7, 100)


# 13


# def factorial(n):
#     k = 1
#     for i in range(1, n + 1):
#         k *= i
#     print(k)


# num = int(input("Number: "))
# factorial(num)


# 14


# def area():
#     figure = input("Figure: ")
#     if figure == "rectangle":
#         rectangle()
#     elif figure == "circle":
#         circle()
#     elif figure == "triangle":
#         triangle()
#     else:
#         print("Unknown figure")


# def rectangle():
#     a = int(input("First side: "))
#     b = int(input("Second side: "))
#     print(f"S = {a * b}")


# def circle():
#     r = int(input("Radius: "))
#     print(f"S = {math.pi * r ** 2}")


# def triangle():
#     a = int(input("First side: "))
#     b = int(input("Second side: "))
#     c = int(input("Third side: "))
#     if triangle_true(a, b, c):
#         p = (a + b + c) / 2
#         s = math.sqrt(p * (p - a) * (p - b) * (p - c))
#         print(f"S = {s}")
#     else:
#         print("Треугольник не существует")


# def triangle_true(a, b, c):
#     if a < b + c and b < a + c and c < a + b:
#         return True
#     else:
#         return False


# area()
