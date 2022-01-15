import random
x = int(input("Введите кол-во элементов"))
arr = [random.randint(0,15) for i in range(x)]
n = 1
for c in arr:
    n *= c
print(n)
