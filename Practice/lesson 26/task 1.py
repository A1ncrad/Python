class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

        
    def hello(self):
        print(f"Hello {self.name} {self.surname}. Age: {self.age}")


class Student(Human):
    pass


n = input("Введите своё имя: ")
s = input("Введите свою фамилию: ")
a =int(input("Введите свой возраст: "))

s1 = Student(n, s, a)
s1.hello()
