users = ["user_1", "user_2", "user_3", "user_4", "user_5"]
good_users = []
while users:
    i = users.pop(0)
    good_users.append(i)
    print(f"Пользователь {i} проверен")
print("Список проверенных пользователей:")
print("\t\t\t\t", good_users)
