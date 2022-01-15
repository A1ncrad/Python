class User:
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


user_1 = User("Timur", "Bratcev", 14, "male")

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.info_login_attempts()
user_1.reset_login_attempts()
user_1.info_login_attempts()
