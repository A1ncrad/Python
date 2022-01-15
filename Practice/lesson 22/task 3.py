def gen(n):
    a, b = 1,0
    for i in range(n):
        yield b
        a += b
        b = a + b
        yield a

n = int(input("Введите количество чисел: "))
y = gen(n)
for j in gen(n):
    print(next(y))
