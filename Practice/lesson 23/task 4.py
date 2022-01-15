a = int(input("Введите первое число: "))
b=int(input("Введите второе число: "))

s = lambda a, b : a + b
s1 = lambda a, b : a - b
s2 = lambda a, b : a * b
s3 = lambda a, b : a / b

print(f"Сумма: {s(a, b)}")
print(f"Разница: {s1(a, b)}")
print(f"Произведение: {s2(a, b)}")
print(f"Деление: {s3(a, b)}")
