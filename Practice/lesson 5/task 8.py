s = int(input("Укажите количество денег на счету: "))
p = int(input("Укажите процент: "))
year=int(input("Укажите месяц снятия: "))
if year > 11 and year < 24:
    s = s + s * (p / 100)
    print(f"Ваша сумма равна:{s}")
elif year > 23 and year < 37:
    s = s + s * (p / 100)
    s = s + s * (p / 100)
    print(f"Ваша сумма равна:{s}")
elif year > 36 and year < 49:
    s = s + s * (p / 100)
    s = s + s * (p / 100)
    s = s + s * (p / 100)
    print(f"Ваша сумма равна:{s}")
else:
    print(f"Ваша сумма равна:{s}")
