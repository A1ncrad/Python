models = ['car','ruchka','karandash','iphone','dolar']
ready_models = []
def prepare(a, b):
    while models:
        del_models = a.pop()
        b.append(del_models)
        print(b)
def printing(b):
    for i in b:
        print(f"Напечеталась модель {i.title()}")
prepare(models, ready_models)
printing(ready_models)
