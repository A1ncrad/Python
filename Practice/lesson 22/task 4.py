def gen():
    for i in langs:
        yield i


langs = ["Python", "JS", "C++", "C", "Java"]
for j in gen():
    print(j)
