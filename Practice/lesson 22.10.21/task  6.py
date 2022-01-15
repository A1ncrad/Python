def greet_user(username, s_name):  
    print(f"Hello!{username.title()} {s_name.title()}")
name = input("Введите имя -->")
name_user = input("Введите фамилию  -->")
greet_user(name, name_user)
