class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person created!")


    def info(self):
        print(f"Name: {self.name} \nAge: {self.age}")


    def hello(self):
        print(f"{self.name} says hello!")


class Student(Human):
    def __init__(self, name, age, course, mark):
         super().__init__(name, age) # Или: Human.__init__(self, name, age, course, mark)                                
         self.course = course
         self.mark = mark


    def study(self):
        print(f"Name student: {self.name} - studing")


    def hello(self):
        print(f"Student created, {self.name} is {self.age}")


    def info_study(self):
        print(f"Course: {self.course}\nMark: {self.mark}")


class Teacher(Human):
    def teach(self):
        print(f"Name teacher: {self.name} - teahing")

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
course = input("Введите курс обучения: ")
mark = input("Введите средний балл: ")
s1 = Student(name, age, course, mark)
s1.info()
s1.study()
s1.hello()
s1.info_study()

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
t1 = Teacher(name, age)
t1.info()
t1.teach()
