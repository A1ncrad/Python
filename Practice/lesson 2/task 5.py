number = int(input("number = "))
p = 0.5
s = 0
for i in range(1 , number + 1):
    s += p
    p /= 2
    print(s)
print(s)
