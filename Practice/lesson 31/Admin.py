from User import User

class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add massage", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print("Admin privileges:")
        for n, item in enumerate(self.privileges):
            print(f"{n + 1}. {item}")
        
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.priv = Privileges()
