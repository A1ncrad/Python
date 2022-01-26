class Restaurant:
    """Class Restaurant using to view info about restaurants.

    Attributes
    __________
    restaurant_name : str
        name of restaurant
    cuisine_type : str
        type of restaurant cuisine
    number_served : int
        number of served clients

    Methods
    _______
    describe_restaurant()
        Show info about restaurant
    open_restaurant()
        Print that restaurant was open
    describe_number_served()
        Show number of served clients
    set_number_served(number)
        Set number of served clients
    increment_number_served(num)
        Increases number of served clients by 1
    """

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

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    """Class IceCreamStand using for view info about icecream stand.

    Attributes
    __________
    inherit all attributes of class Restaurant
    flavors : list
        icecream flavors list

    Methods
    _______
    Inherit all methods of class Restaurant
    info_flavors()
        show list of icecream flavors
    """

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry"]
        self.number_serverd = 0

    def info_flavors(self):
        print("Вкусы мороженого:")
        for i in self.flavors:
            print("\t" * 4 + i)
