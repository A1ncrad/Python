def make_album(sing, alb, number = "None"):
    music = {
        "singer":sing,
        "album":alb,
        "soundtracks":number
        }
    return music
input_name = input("Enter name of any singer:")
input_album = input("Enter his(her) album:")
result1 = make_album(input_name, input_album)
print(result1)
input_name = input("Enter name of any singer:")
input_album = input("Enter his(her) album:")
result2 = make_album(input_name, input_album)
print(result2)
input_name = input("Enter name of any singer:")
input_album = input("Enter his(her) album:")
result3 = make_album(input_name, input_album)
print(result3)
input_name = input("Enter name of any singer:")
input_album = input("Enter his(her) album:")
result4 = make_album(input_name, input_album, "2")
print(result4)
print("All albums:")
print(result1)
print(result2)
print(result3)
print(result4)

    
