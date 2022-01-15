arr_1 = [6, 20, 7, 8]
arr_2 = ["key_1", "key_2", "key_3", "key_4"]
s = int(input("Введите степень:"))
diction = {key:value**s for key, value in zip(arr_2,arr_1) }
for key, value in diction.items():
    print(f"Я знаю твой ключ – {key}, его значение является - {value}")
