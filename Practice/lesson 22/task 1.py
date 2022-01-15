def gen():
    for i in lst:
        yield i
    
lst = ["a", "b", "c", "d"]
y = gen()
print(next(y))
print(next(y))
print(next(y))
print(next(y))
