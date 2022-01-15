import random


n = int(input("Введите число строк: "))
m = int(input("Введите количество столбцов: "))
matrix = [[random.randint(0, 9) for j in range(m)] for i in range(n)]

print(matrix)
print('-' * 60)

for i in matrix:
    print(f"|{i}|")

d = [matrix[i][g] for i in range(n) for g in range(m) if i == g]

print(f"Главная диагональ: {d}")
print('-' * 20)
