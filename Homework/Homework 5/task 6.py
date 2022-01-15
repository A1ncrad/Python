guchka = {
    "animal":"dog",
    "owner":"ivan"
    }
sharik = {
    "animal":"dog",
    "owner":"anton"
    }
kesha = {
    "animal":"parrot",
    "owner":"andrey"    
    }
pets = [guchka, sharik, kesha]
i = 0
while i < len(pets):
    print(pets[i])
    x = pets[i]
    print("Информация о питомце:")
    for inf in x.values():
        print("\t" * 2 + inf.title())
    i += 1
    
