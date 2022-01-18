class Title:
    def __init__(self):
        self.enter = ""

    def get_enter(self):
        enter = input("Введите любой текст:")
        self.enter = enter

    def text_to_title(self):
        word = ""
        for i in self.enter:
            word += i.title()
        print(word)


text_1 = Title()
text_1.get_enter()
text_1.text_to_title()
