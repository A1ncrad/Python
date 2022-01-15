eat = ['pizza', 'falafel', 'carrot cake']
friend_eat = eat[:]
a = input("Введите любимую еду друга")
friend_eat.append(a)
print("Блюда которые нравятся мне:")
for i in eat:
    print("\t", i.title())
print("Блюда которые нравятся моему другу:")
for b in friend_eat:
    print("\t", b.title())
