def gen():
    yield
    print("Первый перебор")
    yield
    print("Второй перебор")
    yield
    print("Третий перебор")
    yield

y = gen()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
