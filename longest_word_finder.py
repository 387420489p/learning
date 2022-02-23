def leghosszabb_szo(szoveg):
    szavak = szoveg.split(" ")
    leghosszabb = ("")
    for szo in szavak:
        if len(szo) > len(leghosszabb):
           leghosszabb = szo
    return leghosszabb


text = input("Type your text here to find the longest word in it! \n")
print(leghosszabb_szo(text))
