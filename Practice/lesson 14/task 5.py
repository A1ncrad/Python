def month_month(n, a):
    for p, i in season.items():
        if n in p:
            a = i
            break
        elif n > 12:
            #print(none)
            break
    return a

none = f"Такого месяца нет"
season= {
        (12, 1, 2): 'Winter',
        (3, 4, 5): 'Spring',
        (6, 7, 8): 'Summer',
        (9, 10, 11): 'Autumn'
    }
number= int(input("Введите число месяца:"))
print(month_month(number, none))
