n = int(input("Сколько будет n слогаемых"))
s=0
a=1/2
i=1
while i<=n:
    s+=a
    i+=1
    a/=2
    print(s)
print(s)
