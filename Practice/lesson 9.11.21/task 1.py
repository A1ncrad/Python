pizza={
    'Four cheese':['cheese', 'chiken', 'tomatoes'],
    'Paperroni':['kolbasa', 'cheese', 'tomatoes', 'souce']
    }
for p, i in pizza.items():
    print('-'*30)
    print(f"Вы заказали {p}: ")
    for value in i:
        print(f"\t\t\t-{value.title()}")
