# 1


def greet_user(name):
    print(f"Hello {name}")


greet_user("Timur")

# 2


def copy(line, n):
    print(line * n)


copy("Hello", 10)

# 3


def max_number(a, b):
    if a > b:
        print(f"{a} > {b}")
    elif a < b:
        print(f"{a} < {b}")
    else:
        print("equal")


max_number(10, 11)

# 4


def max_of_three(a, b, c):
    x = max(a, b)
    y = max(x, c)
    print(y)


max_of_three(10, 11, 12)

# 5


def triangle_true(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        print("Существует")
    else:
        print("Не существует")


triangle_true(10, 15, 20)


# 6

def connect_word(first, second):
    a = [first, second]
    print(" ".join(a))


connect_word("Hello", "World!")

# 7


def calculator(operand, n, operator):
    if operator == "+":
        print("{0:.2f}".format(operand + n))
    elif operator == "-":
        print("{0:.2f}".format(operand - n))
    elif operator == "/":
        print("{0:.2f}".format(operand / n))
    elif operator == "*":
        print("{0:.2f}".format(operand * n))
    else:
        print("Unkown operator")


calculator(2, 7, "/")

# 8


def tags(tag, string):
    tag = f"<{tag}>"
    result = tag + string + tag
    print(result)


tag = input("type tag")
string = input("type content")
tags(tag, string)

# 9

year_time = {
    "winter": (12, 1, 2),
    "spring": (3, 4, 5),
    "summer": (6, 7, 8),
    "autumn": (9, 10, 11)
}


def time_of_year(n):
    for key, value in year_time.items():
        if n in value:
            print(key)


month = int(input("Input number of month"))
time_of_year(month)

# 10



