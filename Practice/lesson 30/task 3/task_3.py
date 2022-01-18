class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"\nName of shop: {self.shop_name}, type of shop: {self.store_type}, types of products: {self.number_of_units}")

    def open_shop(self):
        print(f"\nOnline shop {self.shop_name} was open")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, number):
        self.number_of_units += number


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discount_products(self):
        print("All discount products:")
        for i in self.discount_products:
            print(i)


store = Shop("Amazon", "ishop")
store_2 = Shop("Ebay", "ishop")
store_discount = Discount("Rozetka", "ishop", ["apple", "pen", "iphone"])

print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()
store_2.describe_shop()
print(store.number_of_units)
store.number_of_units = 10
print(store.number_of_units)
store.set_number_of_units(5)
print(store.number_of_units)
store.increment_number_of_units(10)
store.describe_shop()

store_discount.get_discount_products()
