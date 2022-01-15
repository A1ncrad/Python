def pizza(*nazvanie):
    print(f"Вы выбрали такие пиццы:")
    for i in nazvanie:
        print(f"- {i.title()}")    
pizza('gavai')
pizza('peperonni', '4 chees', 'myasnaya')
