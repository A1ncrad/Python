a = int(input("a: "))
p = int(input("%: "))
for i in range(5):
    i += 1
    a = a + a * (p / 100)
    print(int(a))
