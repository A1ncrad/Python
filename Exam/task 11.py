dic = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
    }
for i in dic.values():
    if i % 2 == 0:
        print(f"{i} - even")
    elif i == 0:
        print(f"{i} - zero")
    else:
        print(f"{i} - odd")
