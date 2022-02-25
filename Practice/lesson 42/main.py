import math


# 1

# r = int(input("Введите радиус круга: "))
# s = math.pi * r ** 2
# print("Площадь круга равна {0:.5f}".format(s))

# 2

# password = input("Input your password: ")
# if len(password) < 8:
#     print("Your password too short")
# else:
#     try:
#         int(password)
#         print("password must have minimum a one letter")
#     except ValueError:
#         print("Your password is correct")

# 3

# cash = int(input("How many cash do you have?\n--"))
# if cash > 1000:
#     print("You cant take a credit")
# else:
#     print("Take you're credit")

# 4

# n = int(input("Input your mark: "))
# if 12 >= n > 9:
#     print("You are good student")
# elif 9 >= n > 6:
#     print("Yoa are normal student")
# elif 6 >= n > 3:
#     print("You are bad student")
# elif 3 >= n > 0:
#     print("You are very bad student")
# else:
#     print("You are lie")

# 5

# x = int(input("Input number: "))
# y = int(input("Input number: "))
# if x > y:
#     z = math.sqrt(x * y)
#     print(z)
# else:
#     z = math.log(x + y)
#     print(z)

# 6

# c = int(input("Input temperature: "))
# if c > 20:
#     print("on")
# else:
#     print("off")

# 7

# n = int(input("number: "))
# if n % 2 == 0:
#     print("Второй")
# else:
#     print("Первый")

# 8

# a, b, c = int(input("Input side: ")), int(input("Input side: ")), int(input("Input side: "))
# if a < b + c and b < a + c and c < a + b:
#     print("Possible")
# else:
#     print("Impossible")

# 9

# x = int(input("Input x: "))
# y = int(input("Input y: "))
# if x > 0 and y > 0:
#     print("1 четверть")
# elif x < 0 < y:
#     print("2 четверть")
# elif x < 0 and y < 0:
#     print("3 четверть")
# elif x > 0 > y:
#     print("4 четверть")
# else:
#     print("На одной из кординатных прямых")

# 10

# x = int(input("Input x: "))
# if x > 0:
#     y = 2 * x - 10
#     print(y)
# elif x < 0:
#     y = 2 * math.fabs(x) - 1
#     print(y)
# else:
#     y = 0
#     print(y)

