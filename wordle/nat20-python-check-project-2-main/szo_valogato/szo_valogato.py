# A magyar szavakat (161,745 db) innen vettük:
# https://gist.github.com/Konstantinusz/f9517357e46fa827c3736031ac8d01c7

with open("magyar-szavak.txt", "r", encoding="utf-8") as f:
    szavak = f.readlines()

wordlist = []

for szo in szavak:
    szo = szo.strip()               # sorvég levágás
    if szo.isalpha():               # kötőjeles, hibás szavak kiszűrése
        if len(szo) == 5:           # 5 betűs szavak kigyűjtése
            wordlist.append(szo)    # appendelés

wordlist_set = sorted(set(wordlist))# ismétlődések kiszűrése & ABC sorrend

with open("input_words.txt", "w", encoding="utf-8") as w:
    w.write("\n".join(wordlist_set).lower())
