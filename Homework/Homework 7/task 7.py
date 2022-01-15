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


class Privileges:
    def __init__(self):
        self.privileges = ["Разрешено банить пользователей", "Разрешено удалять пользователей"]

    def show_privileges(self):
        print("Привелегии Администратора:")
        for i in self.privileges:
            print(i)


class Admin(User):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.admin_privileges = Privileges()


admin_1 = Admin("Timur", "Bratcev", 14, "male")

admin_1.admin_privileges.show_privileges()
