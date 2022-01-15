def describe_city(city, country = "ukraine"):
    location = f"{city.title()} " + f"is in {country.title()}"
    print(location)
describe_city("krivoy rog")
describe_city("lviv")
describe_city("moscva", "russia")
