def leghosszabb_szo():
    szoveg = input("Type your text here to find the longest word in it! \n")
    szavak = szoveg.split(" ")
    leghosszabb = ""
    for szo in szavak:
        if len(szo) > len(leghosszabb):
           leghosszabb = szo

    print(f"Leghosszabb szó: {leghosszabb}")