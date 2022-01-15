class Human:
    def __init__(self, name, surname, age):
        self.name=name
        self.surname=surname
        self.age=age

        
    def hello(self):
        print(f"Hello {self.name} {self.surname}. Age: {self.age}")


class Student(Human):
    def study(self):
        print(f"{self.name} studies")


class Teacher(Human):
    def teach(self):
        print(f"{self.name} teaches web-development")


n = input("Введите своё имя: ")
s = input("Введите свою фамилию: ")
a = int(input("Введите свой возраст: "))

s1 = Student(n, s, a)
s1.hello()
s1.study()

n1 = input("Введите имя учителя: ")
s1 = input("Введите фамилию учитиеля: ")
a1 = int(input("Введите возраст учителя: "))
t1 = Teacher(n1, s1, a1)
t1.hello()
t1.teach()
