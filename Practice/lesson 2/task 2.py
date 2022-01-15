number = int(input('Сумма: '))
p = int(input('Процент: '))
x = int(input('Через сколько месяцев хотите забрать сумму: '))
if x > 12 :
    number = number + number * (p / 100)
    print(number)
else:
     print(number)
