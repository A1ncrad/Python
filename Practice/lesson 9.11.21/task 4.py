def month(a):
    for p, i in season.items():
        if a in p:
            print(i)
        else:
            print('Нету такого месяца')
            break
season={
    (12, 1, 2):'Winter',
    (3, 4, 5):'Spring',
    (6, 7, 8):'Summer',
    (9, 10, 11):'Autumn'}
number=int(input('Введите номер месяца: '))
month(number)
