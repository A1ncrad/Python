class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторона: {self.restaurant_name}\nТип кухни: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} открылся!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]

    def info_flavors(self):
        print("Вкусы мороженого:")
        for i in self.flavors:
            print("\t" * 4 + i)


restaurant_1 = IceCreamStand("Ice Cream", "None")

restaurant_1.info_flavors()
