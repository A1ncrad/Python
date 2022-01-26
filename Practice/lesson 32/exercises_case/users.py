class User:
    """Class Users using for register users.

    Attributes
    __________
    first_name : str
        name of user
    last_name : str
        surname of user
    age : int
        age of user
    gender : str
        gender of user
    login_attempts : int
        login attempts of user

    Methods
    _______
    describe_user()
        Print info about user
    greet_user()
        Greet user
    increment_login_attempts()
        Increases value of login attempts by 1
    reset_login_attempts()
        Reset value of login attempts
    info_login_attempts:
        Show value of login attempts
    """
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"Имя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nПол: {self.gender}\n")

    def greet_user(self):
        print(f"Hello!{self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def info_login_attempts(self):
        print(f"Попытки входа: {self.login_attempts}")


class Privileges:
    """Privileges of admin user.

    Attributes
    __________
    privileges : list
        admin privileges list

    Methods
    _______
    show_privileges()
        Print list of admin privileges
    """

    def __init__(self):
        self.privileges = ["Разрешено банить пользователей", "Разрешено удалять пользователей"]

    def show_privileges(self):
        print("Привелегии Администратора:")
        for i, item in enumerate(self.privileges):
            print(f"{i + 1}. {item}")


class Admin(User):

    """Special type of users.

    Attributes
    __________
    inherit all attributes of class User
    admin_privileges :
        privileges of admin user

    Methods
    _______
    Inherit all methods of class User
    """

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.admin_privileges = Privileges()
        self.login_attempts = 0
