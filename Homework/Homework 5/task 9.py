kiev = {
    "country":"ukraine",
    "population":"2,8m",
    "fact":"the capital of ukraine"
    }
krivoy_rog = {
    "country":"ukrainee",
    "population":"600k",
    "fact":"city of metallurgy"
    }
paris = {
    "country":"france",
    "population":"2,1m",
    "fact":"the capital of france"
    }
cities = {
    "kiev":kiev,
    "krivoy rog":krivoy_rog,
    "paris":paris
    }
for i in cities.keys():
    print(i.title() + ":")
    print(f"\t{cities[i]}")
