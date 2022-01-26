from exercises_case import *


usr = users.User("Timur", "Bratcev", 14, "male")
adm = users.Admin("Den", "Dmitriev", 24, "male")
# User
usr.increment_login_attempts()
usr.greet_user()
usr.describe_user()
usr.info_login_attempts()
usr.reset_login_attempts()
usr.info_login_attempts()
# Admin
adm.increment_login_attempts()
adm.greet_user()
adm.admin_privileges.show_privileges()
adm.describe_user()
adm.info_login_attempts()
adm.reset_login_attempts()
adm.info_login_attempts()

res = restaurants.Restaurant("Kozak", "Ukraine cuisine")
ice = restaurants.IceCreamStand("Ice", "icecream")
# Restaurant
res.open_restaurant()
res.describe_restaurant()
res.increment_number_served(5)
res.increment_number_served(1)
res.describe_number_served()
res.set_number_served(10)
res.describe_number_served()
# Icecream stand
ice.open_restaurant()
ice.describe_restaurant()
ice.info_flavors()
ice.increment_number_served(2)
ice.increment_number_served(4)
ice.describe_number_served()
ice.set_number_served(12)
ice.describe_number_served()
