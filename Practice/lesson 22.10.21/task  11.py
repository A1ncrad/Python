def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
t = input("Введите имя ваше -- ")
g = input("Введите вашу фамилию -- ")
musician = get_formatted_name(t, g)
print(musician)
