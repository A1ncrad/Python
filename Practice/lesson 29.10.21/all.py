def pechat(arr_models, arr_pustoy):
    while arr_models:
        ready_models = arr_models.pop(0)
        arr_pustoy.append(ready_models)
        print(arr_pustoy)

def Print(arr_pustoy):
    for text in arr_pustoy:
        print(f"объект {text} - напечатался")
