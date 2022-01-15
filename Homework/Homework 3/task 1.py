def make_shirt(size = "l", text = "i love python"):
    result = f"Размер вашей футболки:{size.title()}" + f"\nТекст на вашей футболке:{text.title()}"
    print(result)
make_shirt()
input_size = input("Введите ваш размер:")
input_text = input("Введите любой текст или фразу:")
make_shirt(input_size, input_text)


