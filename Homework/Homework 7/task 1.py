class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторона: {self.restaurant_name}\nТип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открылся!")


restaurant = Restaurant("Ян-Дзи", "Китайская кухня")
restaurant2 = Restaurant("Козак", "Украинская кухня")
restaurant3 = Restaurant("Стейк хаус", "Американская кухня")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant.open_restaurant()
