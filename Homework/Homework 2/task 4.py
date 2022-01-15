pizza = []
active = 0
while active == 0:
    if active == 1:
        break
    inlet = input("Введите ваше дополнение для пиццы(для выхода введите quite)")
    if inlet == "quite":
        print("Ваши дополнения:")
        for i in pizza:
            print(f"{i.title()}")
        inlet = input("Вы уверены что все добавили?(для подтверждения введите yes или отмените с помощью no)")
        if inlet == "yes":
            print("Ваш заказ принят ожидайте")
            active = 1
        else:
            continue
    else:
        pizza.insert(0, inlet)
        print(f"Вы добавили в пиццу {pizza[0].title()}")
        
        
