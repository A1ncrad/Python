import random
numbers = [random.randint(1,100) for i in range(1, 30)]
print(numbers)
for n in numbers:
    if n % 2 == 0:
        print(n)
    else:
        print(f"{n} не делится нацело на 2")
