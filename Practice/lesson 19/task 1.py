a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = [items if items < 5 else "False" for items in a]
print(new)
