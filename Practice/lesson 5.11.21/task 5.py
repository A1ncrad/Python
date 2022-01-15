name_users = {"Ivan": 15, "Denis": 24, "Renat": 15, "Kirill": 49, "Nela": 18}
user_auto = {"Zhigul": 1990, "Ferrari": 2021, "Volkswagen": 2020}
data_user = name_users|user_auto
print(data_user)
name_users|=user_auto
print(name_users)
keys = name_users.keys()
print(keys)
for a in keys:
    print(a)
values = name_users.values()
for x in values:
    print(x)

for s, y in name_users.items():
    print(f"Ключи: {s}, Значения: {y}")
get_user = name_users.get("Denis", "User not founded")
print(get_user)
