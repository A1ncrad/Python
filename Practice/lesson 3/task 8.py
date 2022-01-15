mach = ["bmw", "audi", "benz"]
message = f"Я хочу расмотреть марку машини без марки {mach[1].title()}"
print(message)
del mach[1]
print(mach)
