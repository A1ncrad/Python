num = ("3", "7", "666", "2", "13", "10", "4", "100", "256", "64")
favorite_num = {
    "anton":num[0:2],
    "ivan":num[2:4],
    "ilya":num[4:6],
    "andrey":num[6:8],
    "vlad":num[8:10]
    }
for x in favorite_num.keys():
    print(x.title() + ":")
    print("\t", favorite_num[x])
    
