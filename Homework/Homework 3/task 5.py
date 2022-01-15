def make_album(sing, alb):
    music = {
        "singer":sing,
        "album":alb,
        }
    return music
while True:
    input_name = input("Enter name of any singer (if you want quite enter q):")
    if input_name == "q":
        print("Good bye!")
        break
    else:
        input_album = input("Enter his (her) album (if you want quite enter q):")
        if input_album == "q":
            print("Good bye!")
            break
        else:
            print(make_album(input_name, input_album))
        
