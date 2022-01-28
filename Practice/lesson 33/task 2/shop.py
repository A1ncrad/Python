class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Name : {self.shop_name}\nStore type :{self.store_type}")

    def open_shop(self):
        print(f"{self.shop_name} was open")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, number):
        self.number_of_units += number

    def info_number_of_units(self):
        print(self.number_of_units)
