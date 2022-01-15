import random
n = int(input("строки"))
m = int(input("столбцы"))
k = int(input("строка"))
string = k - 1
p = int(input("колонка"))
column = p - 1
print("элемент:")
a, r = int(input("по строке")), int(input("по столбцу"))
a -= 1
r -= 1
arr = [[random.randint(0,9) for g in range(m)] for i in range(n) ]
for x in arr:
    print(x)
diagonal = [arr[i][g] for i in range(n) for g in range(m) if i == g]
print(f"Главная диагональ:{diagonal}")
stroka = [arr[i][g] for i in range(n) for g in range(m) if i == string]
print(f"{k} строка:{stroka}")
colonka = [arr[i][g] for i in range(n) for g in range(m) if g == column]
print(f"{p} колонка:{colonka}")
print(arr[a][r])
