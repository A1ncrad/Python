from exercises_case import *


info = f"""Class Restaurant info :\n\n{restaurants.Restaurant.__doc__}\n\nClass IceCreamStand info :\n
{restaurants.IceCreamStand.__doc__}\n\nClass User info :\n\n{users.User.__doc__}\n\nClass Admin info :\n
{users.Admin.__doc__}\n\nClass Privileges info :\n\n{users.Privileges.__doc__}"""

with open("documentation.txt", "w") as i:
    i.write(info)
