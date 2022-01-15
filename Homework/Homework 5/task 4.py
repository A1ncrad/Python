rivers = {
    "nile":"egypt",
    "amazon":"columbia",
    "yangtze":"china"
    }
for river in rivers.keys():
    print(f"The {river.title()} runs trought {rivers[river].title()}")
print("\n" + "Rivers:")
for r in rivers.keys():
    print("\t" + r.title())
print("\n" + "Countries:")
for country in rivers.values():
    print("\t" + country.title())

