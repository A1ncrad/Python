subject = ["История", "Математика", "География", "Информатика", "Физ-ра"]
n = int(input("Какой урок вас интересует: "))
if n == 1:
    print(subject[0])
elif n == 2:
    print(subject[1])
elif n == 3:
    print(subject[2])
elif n == 4:
    print(subject[3])
elif n == 5:
    print(subject[4])
else:
    print("У 9 класса 5 уроков")
