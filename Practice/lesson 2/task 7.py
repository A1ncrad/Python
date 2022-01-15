x = int(input("Введите ваш рост: "))
if x > 180:
    print("Мальчик")
elif x <= 180 and x > 150 :
    print("Девочка")
elif x < 1:
    print("Такого роста быть не может!")
else:
    print('Ребенок')
