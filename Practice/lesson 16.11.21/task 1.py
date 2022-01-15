num_1 = [3,2,1]
num_2 = [1,2,3]
num_3 = [(i, n) for i in num_1 for n in num_2 ]
print(num_3)
for x in num_3:
    print(x)
