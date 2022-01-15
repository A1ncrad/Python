def greet_user(username): 
    print(f"Hello!{username.title()}")
name = input("Введите имя -->")
greet_user(name)
