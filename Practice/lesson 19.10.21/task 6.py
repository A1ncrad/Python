n = int(input("Введите число ")) 
i=0
while n>0:
    n//=10   
    i+=1
print(f"Цифр в числе -> {i}")
