s = 5000
percent = 20
year = int(input("Укажите месяц снятия: "))
if year > 11 and year < 24:
    s = s + s * (percent / 100)
    print(f"Ваша сумма равна:{s}")
elif year > 23:
    s = s + s * (percent / 100)
    s = s + s * (percent / 100)
    print(f"Ваша сумма равна:{s}")
else:
    print(f"Ваша сумма равна:{s}")
    
