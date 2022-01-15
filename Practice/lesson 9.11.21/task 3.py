players={
    'user_0':{
        'first_name':'Renat',
        'last_name':'Net',
        'age':14,
        'IP':'49.15.46',
        'country':'UK'},
    'user_1':{
        'first_name':'Vania',
        'last_name':'Tsurkan',
        'age':15,
        'IP':'48.26.99',
        'country':'Ukraine'},
    'user_2':{
        'first_name':'Kirill',
        'last_name':'Antonov',
        'age':15,
        'IP':'35.98.35',
        'country':'Japan'}
    }
for p, i in players.items():
    print("-"*30)
    print(f"Игрок под именем {p}: ")
    players_info = f"{i['first_name']} {i['last_name']}"
    age = i['age']
    ip = i['IP']
    country = i['country']
    print(f"\tИмя фамилия игрока: {players_info.title()}")
    print(f"\tВозраст: {age}")
    print(f"\tIP: {ip}")
    print(f"\tСтрана: {country}")
