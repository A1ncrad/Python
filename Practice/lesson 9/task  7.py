def describe_pet(animal_type, pet_name):
    print(f"\nУ меня есть {animal_type}.")
    print(f"Мой {animal_type} и его зовут {pet_name.title()}.")
t_a = input("Ведите какое у вас животное ->")
p_name = input("Введите как зовут вашего животного ->")
describe_pet(t_a, p_name)
