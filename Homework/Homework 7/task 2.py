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


user_1 = User("Timur", "Bratcev", 14, "male")
user_2 = User("Den", "Dmitriev", 24, "male")

user_1.describe_user()
user_2.describe_user()
user_1.greet_user()
user_2.greet_user()
