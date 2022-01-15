while True:
    x = input("Введите ваш возраст(для выхода введите quite)")
    if x == "quite":
        break
    elif int(x) < 3:
        print("Для вас билет бесплатный")
    elif 3 <= int(x) <= 12:
        print("Для вас билет стоит 10$")
    else:
        print("Для вас билет стоит 15$")
        
