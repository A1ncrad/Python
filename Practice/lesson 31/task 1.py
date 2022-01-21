from User import User
from Admin import Admin

  
user = User("Timur", "Bratcev", 14)
admin = Admin("Den", "Dmitriev", 24)

user.describe_user()
user.greeting_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

admin.priv.show_privileges()
