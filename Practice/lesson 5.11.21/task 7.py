name_users = {"Ivan": 15, "Denis": 24, "Renat": 15, "Kirill": 49, "Nela": 18}
user_auto = {"Zhigul": 1990, "Ferrari": 2021, "Volkswagen": 2020}
about_life = [name_users, user_auto]
print(about_life)
for i in about_life:
    print(i)
empty = []
for a in range(3):
    new_item = {"Color": "gray", "Speed": 50, "Temprature": -10}
    empty.append(new_item)
    print(empty)
for b in empty[:2]:
    if b["Color"] == "gray":
        b["Color"] = "black"
        b["Speed"] = 100
        b["Temprature"] = 25
for c in empty:
    print(c)
