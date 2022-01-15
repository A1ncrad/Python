class Car:
    def __init__(self, model, year, mark):
        self.model = model
        self.year = year
        self.mark = mark
        self.odometer = 0


    def get_descript_name(self):
        print(f"Mark of car: {self.mark}, model: {self.model}, year: {self.year}")


    def read_odometer(self):
        print(f"Пробег вашей {self.mark}, равен: {self.odometer} miles")


    def update_odometer(self, n):
        if n < self.odometer:
            print("пробег скинуть невозможно")
        else:
            self.odometer = n


    def increement_odometer(self, m):
        self.odometer += m


class ElectroCar(Car):
    def __init__(self, model, year, mark):
        super().__init__(model, year, mark)
        self.battery = 100


    def get_descript_name(self):
        print(f"Mark of car: {self.mark}, model: {self.model}, year: {self.year}, battery:{self.battery} mA")

    def battery_change(self, y):
        self.battery = y
        print(f"бъем батареи равен: {self.battery}")

    def coins(self, cost):
        if cost > 1000000:
            print("Take your car")
        else:
            print("Goodbye!")
            

y = int(input("Введите объем батареи: "))        
my_new_car = ElectroCar("s", 2020, "tesla")
my_new_car.battery_change(y)
my_new_car.get_descript_name()

n = int(input("Ведите пробег: "))
m = int(input("Проеханное растояние(miles) :"))
#my_new_car.odometer = 23

my_new_car.update_odometer(n)
my_new_car.increement_odometer(m)
my_new_car.read_odometer()
x = int(input("За какую сумму вы хотите купить электрокар? "))
my_new_car.coins(x)
