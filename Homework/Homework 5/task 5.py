ivan = {
    "first_name":"Ivan",
    "last_name":"Ivanov",
    "age":"18",
    "city":"Krivoy Rog"
    }
anton = {
    "first_name":"Anton",
    "last_name":"Antonov",
    "age":"24",
    "city":"Kiev"
    }
artur = {
    "first_name":"Artur",
    "last_name":"Arturov",
    "age":"8",
    "city":"Harkov"
    }
people = [ivan, anton, artur]
i = 0
while i < len(people):
    print(people[i])
    x = people[i]
    for v in x.values():
        print(v)
    i += 1
