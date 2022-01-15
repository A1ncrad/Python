def gen():
    k = 1
    while True:
        if k > 1:
            for i in range(2, k):
                if k % i == 0:
                    break
                else:
                    yield k
        k += 1
for j in gen():
    print(j)
