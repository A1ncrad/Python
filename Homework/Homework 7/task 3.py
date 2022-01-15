class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Название ресторона: {self.restaurant_name}\nТип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открылся!")

    def describe_number_served(self):
        print(f"Число обслуженных клиентов: {self.number_served}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, m):
        self.number_served += m


restaurant = Restaurant("Ян-Дзи", "Китайская кухня")

restaurant.describe_number_served()
restaurant.number_served = 5
restaurant.describe_number_served()
n = int(input("Введите число обслуженных клиентов: "))
restaurant.set_number_served(n)
restaurant.describe_number_served()
m = int(input("Сколько клиентов обслужили за день: "))
restaurant.increment_number_served(m)
restaurant.describe_number_served()
