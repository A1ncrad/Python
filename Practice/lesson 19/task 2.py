import random


a = [random.randint(0, 15) for i in range(10)]
print(a)
print(a[0],a[-1])
d = sum(a)
print(d)
