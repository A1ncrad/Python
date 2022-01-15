class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"Имя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}\n")

    def greet_user(self):
        print(f"Hello!{self.first_name}")


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = ["Разрешено банить пользователей", "Разрешено удалять пользователей"]

    def show_privileges(self):
        print("Привелегии Администратора:")
        for i, item in enumerate(self.privileges):
            print(f"{i + 1}.{item}")


admin_1 = Admin("Timur", "Bratcev", 14, "male")

admin_1.show_privileges()
