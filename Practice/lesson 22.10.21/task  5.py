def greet_user(username):   
    print(f"Hello!{username.title()}")
name = input("Введите имя -->")
name_user = input("Введите имя вашего соседа  -->")
greet_user(name)
greet_user(name_user)
