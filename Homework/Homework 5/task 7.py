places = ["the eiffel tower", "the great wall of china", "leaning tower of pisa"]
favorite_places = {
    "ivan":places[2],
    "anton":places[0:2],
    "andrey":places[0:3]
    }
print(favorite_places)
for i in favorite_places.keys():
    print(i.title() + ":")
    print(f"\t{favorite_places[i]}")


