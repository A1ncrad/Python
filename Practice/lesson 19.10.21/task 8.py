while True:
    k = int(input("Введите k (не более 15): "))
    if k<=15:
        break 
p = 1          
i = 1          
while True:    
    p = p*i   
    i = i+1    
    if i>k:
        break      
print("Факториал равен", p)
