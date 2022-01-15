height = int(input("Введите рост: "))
if height > 150 and height < 180:
    print("Это девушка!")
elif height > 179:
    print("Это парень!")
else:
    print("Это ребёнок!")
