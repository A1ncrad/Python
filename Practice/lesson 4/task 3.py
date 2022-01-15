mach = ["bmw", "audi", "mercedes", "ford", "subaru", "chrvrolete"]
print(mach)
message = f"Я хочу рассмотреть марку машины {mach[2].title()}"
print(message)
del_item = mach.pop(2)
print(del_item)
message_1 = f"Я хочу рассмотреть марку машины {mach[2].title()}"
print(message_1)
del_item_1 = mach.pop(2)
print(del_item_1)
message_2 = f"Я хочу рассмотреть марку машины {mach[2].title()}"
print(message_2)
del_item_2 = mach.pop(2)
print(del_item_2)
print(mach)
