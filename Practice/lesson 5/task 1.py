a = float(input("Введите первое число: "))
b = float(input("Введите  второе число: "))
if a > b:
    a = 1
    b = 0
    print(a, b)
elif b > a:
    a = 0
    b = 1
    print(a, b)
else:
    print("Они одинаковые!")
