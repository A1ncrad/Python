class Bot:
    def __init__(self, name, age, country, city, about):
        self.name = name
        self.age = age
        self.country = country
        self.city = city
        self.about = about
    def form(self):
        print(f"Ваша анкета выглядит так:\n\tИмя: {self.name}\n\tВозраст: {self.age}\n\tСтрана: {self.country}\n\tГород: {self.city}\n\tО себе: {self.about}")




while True:
    choice = int(input(f"Введите:\nЦифру `1`, если хотите заполнить анкету!\nЦифру `2`, если хотите изменить анкету!\nЦифру `3`, если всё готово!"))
    if choice == 1:
        print("Заполните анкету:")
        inname = input("Введите своё имя: ")
        inage = int(input("Введите свой возраст: "))
        incountry = input("Введите страну в которой проживаете: ")
        incity = input("Введите город в котором вы проживаете: ")
        about_you = input("Расскажите о себе что-то интересное: ")
        info = Bot(inname, inage, incountry, incity, about_you)
        while True:
            view = input("Если хотите посмотреть вашу анкету введите `Посмотреть`!\nЕсли не хотите просматривать вашу анкету, введите `Готово`")
            if view == "Посмотреть":
                info.form()
                break
            elif view == "Готово":
                print("Ваша анкета сохранена!")
                break
            else:
                print("Введите один из вариантов ответа:")
    elif choice == 2:
        print("Измените свою анкету: \n")
        inname = input("Введите своё новое имя: ")
        inage= int(input("Введите свой новый возраст: "))
        incountry = input("Введите страну в которой проживаете: ")
        incity= input("Введите город в котором вы проживаете: ")
        about_you = input("Расскажите о себе что-то интересное: ")
        info=Bot(inname, inage, incountry, incity, about_you)
        while True:
            view = input("Если хотите посмотреть вашу анкету введите `Посмотреть`! Если не хотите просматривать вашу анкету, введите `Готово`")
            if view == "Посмотреть":
                info.form()
                break
            elif view == "Готово":
                print("Ваша анкета сохранена!")
                break
            else:
                print("Введите один из вариантов ответа: ")
    elif choice==3:
        print("Ваша анкета заполнена!")
        break
    else:
        print("Вы выбрали некорректное число!!!")
