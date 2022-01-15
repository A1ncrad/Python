def gen():
    for i in sqrt:
        yield i

y = gen()
num = [4, 16, 64, 256]
sqrt = [item ** (1/2) for item in num]
k = 0
while k < len(sqrt):
    print(next(y))
    k += 1
