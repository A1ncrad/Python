import random
n=int(input('1'))
m=int(input('2'))
matrix = [[random.randint(0,9) for i in range(m)] for a in range(n)]
print('Matrix ==>')
for b in matrix:
    print(f"\t {b}")
diagonal = [matrix[q][w] for q in range(n) for w in range(m) if q == w]
print(f"Glavnaya diagonal ==> {diagonal}")
string = [matrix[q][w] for q in range(n) for w in range(m) if q == 1]
print(f"Second string ==> {string}")
column = [matrix[q][w] for q in range(n) for w in range(m) if w == 2]
print(f"Third column ==> {column}")
