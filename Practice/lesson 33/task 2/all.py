from shop import Shop


class Discount(Shop):
    def __init__(self, shop_name, store_type):
        super().__init__(shop_name, store_type)
        self.discount_products = ["phone", "apple", "pen"]

    def get_discounts_products(self):
        print("Discount products :")
        for i in self.discount_products:
            print(i)


store = Shop("Rozetka", "ishop")
store2 = Shop("Ekatalog", "ishop")
store_discount = Discount("Amazon", "ishop")

print(store.shop_name)
print(store.store_type)

store.describe_shop()
store.open_shop()
store.info_number_of_units()
store.number_of_units = 2
store.info_number_of_units()
store.set_number_of_units(7)
store.info_number_of_units()
store.increment_number_of_units(5)
store.info_number_of_units()

store2.describe_shop()

store_discount.get_discounts_products()
